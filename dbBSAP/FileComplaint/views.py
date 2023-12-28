from django.contrib import messages
from django.db import connection
from django.http import request
from django.shortcuts import render, redirect
from .forms import ResidentForm, LoginForm
from django.views.generic.base import View
from django.apps import apps

Resident = apps.get_model('CreateAccount', 'Resident')

# Create your views here.


class login(View):
    template_name = "login.html"

    def get(self, request):
        form = LoginForm(request.GET)
        return render(request, self.template_name, {'form': form, 'message': ''})

    def post(self, request):
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        arg = [username, password]

        user = Resident.objects.get(username=username)
        request.session['username'] = user.username

        cursor = connection.cursor()
        cursor.callproc('verifyLogin', arg)
        message = cursor.fetchone()[0]
        cursor.close()
        print(message)
        if message == "Login succesful":

            return redirect('complaint')
        else:
            return render(request, self.template_name, {'form': form, 'message': message})

class ResidentRegistration(View):
    template_name = "register.html"

    def get(self, request):
        register = ResidentForm()
        return render(request, self.template_name, {'form': register})

    def post(self, request):
        register = ResidentForm()
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        birthdate = request.POST['birth_date']
        present_address = request.POST['present_address']

        cursor = connection.cursor()
        args = [username, password, firstname, lastname, birthdate, present_address]
        cursor.callproc('createResident', args)
        result = cursor.fetchall()
        message = result[0][0]
        cursor.close()
        if message == "Successfully created a new account":
            return redirect('login')
        return render(request, self.template_name, {'form': register, 'error_message': message})

    """ Previous implementation
    def get(self, request): 
        form = ResidentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ResidentForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            try:
                Resident.objects.get(username=username)
                message = "Username already exists"
            except Resident.DoesNotExist:
                form.save()
                return redirect('login')
        else:
            messages.error(request, 'Registration invalid. Please try again.')
        return render(request, self.template_name, {'form': form, 'message': message})
        """

class Complaint(View):
    template_name = "complaint.html"
    user = request.session['complainant_id']
    def get(self, request):
        user = request.session['username']

        return render(request, self.template_name)









