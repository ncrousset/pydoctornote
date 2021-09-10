from django.views.generic import CreateView
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import CustomUser as User

from .models import Patient
from .forms import PatientForm


def dashboard(request):
    return render(request, 'app/dashboard.html')


@login_required(redirect_field_name='')
def list_patient_view(request):
    patients = Patient.objects.all()

    patients_dict = {
        'patients': patients,
        'form': PatientForm
    }

    return render(request, 'app/patients_list_view.html', patients_dict)


@login_required(redirect_field_name='')
def patient_view(request, pk: int):

    patient = Patient.objects.get(pk=pk)

    patients_dict = {
        'patient': patient
    }

    return render(request, 'app/patient_view.html', patients_dict)


class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'app/forms/patient_create_form.html'

    def form_valid(self, form):
        form.instance.user_id = User.objects.last()

        return super().form_valid(form)

    def form_invalid(self, form):
        errors = {
            'messages': "Error we can't save the patient"
        }
        redirect('list_patient_view', errors)
        return super().form_invalid(form)
