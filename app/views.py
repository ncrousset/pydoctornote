from .models import Patient
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import PatientForm
from accounts.models import CustomUser as User


def dashboard(request):
    return render(request, 'app/dashboard.html')


def list_patient_view(request):
    patients = Patient.objects.all()

    patients_dict = {
        'patients': patients,
        'form': PatientForm
    }

    return render(request, 'app/patients_list_view.html', patients_dict)


def patient_view(request, pk: int):
    return render(request, 'app/patients_view.html')


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'app/forms/patient_create_form.html'

    def form_valid(self, form):
        form.instance.user_id = User.objects.last()

        return super().form_valid(form)

    def form_invalid(self, form):

        return super().form_invalid(form)
