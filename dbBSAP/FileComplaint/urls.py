from django.urls import path
from . import views


urlpatterns = [
    path('', views.login.as_view(), name='login'),
    path('register/', views.ResidentRegistration.as_view(), name='register'),
    path('complaint/', views.Complaint.as_view(), name="complaint"),
    path('file_complaint/', views.FileComplaint.as_view(), name="filecomplaint")
]