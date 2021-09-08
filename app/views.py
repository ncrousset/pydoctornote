from django.shortcuts import render

from .models import Patient


def dashboard(request):
    return render(request, 'app/dashboard.html')


def list_patient_view(request):
    patients = Patient.objects.all()

    patients_dict = {
        'patients': patients
    }

    return render(request, 'app/patients_list_view.html', patients_dict)
