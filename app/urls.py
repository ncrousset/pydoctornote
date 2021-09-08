from django.urls import path
from .views import dashboard, list_patient_view

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('patients/', list_patient_view, name="list_patients"),
]
