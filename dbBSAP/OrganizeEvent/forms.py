from django import forms
from .models import Event
from django.apps import apps

Organization = apps.get_model('CreateAccount', 'Organization')
Resident = apps.get_model('CreateAccount', 'Resident')

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['eventName', 'organizer', 'details', 'start', 'end', 'event_status', 'location']

class OrgRegisterForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['username', 'password', 'user_type', 'organization_name']

class ResidentRegisterForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = ['username', 'password', 'user_type', 'first_name', 'last_name', 'birth_date', 'present_address']