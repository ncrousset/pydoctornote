from django import forms
from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'birth_date', 'email', 'insurance',
                  'idd', 'phone', 'sex', 'next_appointment', )
