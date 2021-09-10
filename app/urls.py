from django.urls import path, re_path
from .views import (dashboard, list_patient_view,
                    PatientCreateView, PatientUpdateView, patient_view)

urlpatterns = [
    path('', dashboard, name="dashboard"),
    re_path(r'^patients/$',
            list_patient_view, name="list_patients"),
    path('patient/<int:pk>', patient_view, name="detail_patient"),
    path('patients/create/', PatientCreateView.as_view(), name='create_patient'),
    path('patients/update/<int:pk>',
         PatientUpdateView.as_view(), name='update_patient'),
]
