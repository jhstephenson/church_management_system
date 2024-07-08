from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import views as auth_views
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from .models import Calling, Unit, Organization, Position, Leadership
from .forms import CallingForm, UnitForm, OrganizationForm, PositionForm, LeadershipForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

@login_required
def calling_list(request):
    show_all = request.GET.get('show_all') == 'on'
    callings_queryset = Calling.objects.all()
    if not show_all:
        callings_queryset = callings_queryset.filter(leader_and_clerk_resources_updated=False)
    
    # Sort the callings
    callings_queryset = callings_queryset.order_by('unit__name', 'organization__name', 'position__name')
    
    # Pagination
    paginator = Paginator(callings_queryset, settings.CALLINGS_PER_PAGE)
    page = request.GET.get('page')
    try:
        callings = paginator.page(page)
    except PageNotAnInteger:
        callings = paginator.page(1)
    except EmptyPage:
        callings = paginator.page(paginator.num_pages)
    
    return render(request, 'callings/calling_list.html', {
        'callings': callings,
        'show_all': show_all
    })

@login_required
def calling_create(request):
    if request.method == 'POST':
        form = CallingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calling_list')
    else:
        form = CallingForm()
    return render(request, 'callings/calling_form.html', {'form': form})

@login_required
def calling_detail(request, pk):
    calling = get_object_or_404(Calling, pk=pk)
    return render(request, 'callings/calling_detail.html', {'calling': calling})

@login_required
def calling_update(request, pk):
    calling = get_object_or_404(Calling, pk=pk)
    if request.method == 'POST':
        form = CallingForm(request.POST, instance=calling)
        if form.is_valid():
            form.save()
            return redirect('calling_list')
    else:
        form = CallingForm(instance=calling)
    return render(request, 'callings/calling_form.html', {'form': form})

@login_required
def calling_delete(request, pk):
    calling = get_object_or_404(Calling, pk=pk)
    if request.method == 'POST':
        calling.delete()
        return redirect('calling_list')
    return render(request, 'callings/calling_confirm_delete.html', {'calling': calling})

@login_required
@require_http_methods(["GET", "POST"])
def create_reference(request, model_name):
    if model_name == 'unit':
        form_class = UnitForm
        model = Unit
    elif model_name == 'organization':
        form_class = OrganizationForm
        model = Organization
    elif model_name == 'position':
        form_class = PositionForm
        model = Position
    elif model_name == 'leadership':
        form_class = LeadershipForm
        model = Leadership
    else:
        return JsonResponse({'error': 'Invalid model name'}, status=400)

    if request.method == 'POST':
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            try:
                data = json.loads(request.body)
                form = form_class(data)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        else:
            form = form_class(request.POST)

        if form.is_valid():
            new_item = form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'id': new_item.id, 'name': str(new_item)})
            return redirect('calling_list')
        else:
            return JsonResponse({'error': str(form.errors)}, status=400)
    else:
        form = form_class()
    
    return render(request, 'callings/reference_form.html', {'form': form, 'model_name': model_name})

class CustomLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'

class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def admin_redirect(request):
    return redirect('/admin/')