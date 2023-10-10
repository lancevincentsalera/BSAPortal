from django.contrib import admin
from .models import Complaint, ComplaintDetails
# Register your models here.

admin.site.register(Complaint)
admin.site.register(ComplaintDetails)