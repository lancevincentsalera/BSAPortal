from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.login, name="login"),
    path('event',ShowEvents.as_view(), name="event"),
    path('org-event',views.org_event, name="org-event"),
    path('event-add',views.create_event, name="event-add"),
    path('register-org', RegisterOrg.as_view(), name="register-org"),
    path('register-options', views.registerOptions, name="register-options"),
    path('register-resident', RegisterResident.as_view(), name="register-resident"),
]