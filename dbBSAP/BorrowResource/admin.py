from django.contrib import admin
from .models import Resource, BorrowResource
# Register your models here.

admin.site.register(Resource)
admin.site.register(BorrowResource)