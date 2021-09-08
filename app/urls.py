from django.urls import path
from .views import dashboard, list_patient_view, PatientCreateView, patient_view

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('patients', list_patient_view, name="list_patients"),
    path('patient/<int:pk>', patient_view, name="detail_patient"),
    path('patients/create/', PatientCreateView.as_view(), name='create_patient')
]
