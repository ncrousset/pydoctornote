from django.contrib.postgres import search
from django.views.generic import CreateView, UpdateView
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from accounts.models import CustomUser as User

from .models import Patient
from .forms import PatientForm


def dashboard(request):
    return render(request, 'app/dashboard.html')


@login_required(redirect_field_name='')
def list_patient_view(request):

    search = request.GET.get('search')

    if search is not None:
        patients = Patient.objects.filter(
            Q(first_name__icontains=search) | Q(last_name__icontains=search),
        )
    else:
        patients = Patient.objects.all()

    patients_dict = {
        'patients': patients,
        'form': PatientForm
    }

    return render(request, 'app/patients_list_view.html', patients_dict)


@login_required(redirect_field_name='')
def patient_view(request, pk: int):

    patient = Patient.objects.get(pk=pk)

    form = PatientForm(instance=patient)

    patients_dict = {
        'patient': patient,
        'form': form
    }

    return render(request, 'app/patient_view.html', patients_dict)


class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'app/forms/patient_create_form.html'

    def form_valid(self, form):
        form.instance.user_id = self.request.user

        return super().form_valid(form)

    def form_invalid(self, form):
        errors = {
            'messages': "Error we can't save the patient"
        }
        redirect('list_patient_view', errors)
        return super().form_invalid(form)


class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'app/forms/patient_update_form.html'
