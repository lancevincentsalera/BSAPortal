from django.contrib import admin
from .models import HealthCenter, Appointment
# Register your models here.

admin.site.register(HealthCenter)
admin.site.register(Appointment)
