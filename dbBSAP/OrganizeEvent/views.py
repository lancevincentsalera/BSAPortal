from django.shortcuts import render, redirect
from django.apps import apps
from django.views import View

from .forms import *
from .models import Event

Resident = apps.get_model('CreateAccount','Resident')
Admin = apps.get_model('CreateAccount','Admin')
Organization = apps.get_model('CreateAccount','Organization')
HealthCenter = apps.get_model('BookAppointment','HealthCenter')

def registerOptions(request):
    return render(request, "register_options.html", {})


class RegisterOrg(View):
    template = 'org_register.html'

    def get(self, request):
        register = OrgRegisterForm()
        return render(request, self.template, {'form': register})

    def post(self, request):
        register = OrgRegisterForm(request.POST)
        if register.is_valid():
            register.save()
            return redirect(login)

        return render(request, self.template, {'form': register})

class RegisterResident(View):
    template = 'resident_register.html'

    def get(self, request):
        register = ResidentRegisterForm()
        return render(request, self.template, {'form': register})

    def post(self, request):
        register = ResidentRegisterForm(request.POST)
        if register.is_valid():
            register.save()
            return redirect(login)

        return render(request, self.template, {'form': register})

class ShowEvents(View):
    template = 'event.html'
    def get(self, request):
        events = Event.objects.all()
        return render(request, self.template, {'events': events})


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST) #create events
        if form.is_valid():
            form.save()
            return redirect(org_event)  # Redirect to the event list view after creating the event
    else:
        form = EventForm()

    return render(request, 'event_add.html', {'form': form})


def event(request):
    events = Event.objects.all()
    return render(request, 'event.html', {'events': events})

def org_event(request):
    events = Event.objects.all()
    return render(request, 'org_events.html', {'events': events})

def login(request):
    error_message = None  # Initialize error_message

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = None  # Initialize the user variable

        # Check if the user is in the Resident table
        try:
            user = Resident.objects.get(username=username, password=password, user_type="R")
            return ShowEvents.get(ShowEvents, request)
        except Resident.DoesNotExist:
            pass

        # If the user is not in the Resident table, check the Organization table
        if not user:
            try:
                user = Organization.objects.get(username=username, password=password, user_type="O")
                return redirect(org_event)
            except Organization.DoesNotExist:
                pass

        # If the user is not in the Organization table, check the Admin table
        if not user:
            try:
                user = Admin.objects.get(username=username, password=password, user_type="A")
            except Admin.DoesNotExist:
                pass

        if user:
            # User was found in one of the tables, redirect to the success page
            return redirect('event')
        else:
            error_message = "Invalid username or password."

    # If the request is not a POST request or if the user is not found, render the login page with the error message
    return render(request, 'login.html', {'error_message': error_message})


