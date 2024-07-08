from django import forms
from .models import Calling, Unit, Organization, Position, Leadership

class CallingForm(forms.ModelForm):
    class Meta:
        model = Calling
        fields = '__all__'
        widgets = {
            'released_date': forms.DateInput(attrs={'type': 'date'}),
            'high_council_approved': forms.DateInput(attrs={'type': 'date'}),
            'date_called': forms.DateInput(attrs={'type': 'date'}),
            'date_sustained': forms.DateInput(attrs={'type': 'date'}),
            'date_set_apart': forms.DateInput(attrs={'type': 'date'}),
        }

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['name']

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name']

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['name']

class LeadershipForm(forms.ModelForm):
    class Meta:
        model = Leadership
        fields = ['name']