from django.contrib import admin
from django.urls import path, include
from callings import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.calling_list, name='calling_list'),
    path('calling/create/', views.calling_create, name='calling_create'),
    path('calling/<int:pk>/', views.calling_detail, name='calling_detail'),
    path('calling/<int:pk>/update/', views.calling_update, name='calling_update'),
    path('calling/<int:pk>/delete/', views.calling_delete, name='calling_delete'),
    path('create_reference/<str:model_name>/', views.create_reference, name='create_reference'),
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('admin_redirect/', views.admin_redirect, name='admin_redirect'),
]