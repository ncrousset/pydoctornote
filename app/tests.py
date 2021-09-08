from django.http import response
from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Patient


class PatientTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@gmail.com',
            password='test'
        )

        self.patient = Patient.objects.create(
            first_name='Natanael',
            last_name='Acosta',
            birth_date='2021-05-18',
            email='natanael926@gmail.com',
            insurance='454555',
            idd='545456',
            phone='5454545',
            sex='m',
            next_appointment='2021-05-18',
            user_id=self.user
        )

    def test_string_representation(self):
        patient = Patient(first_name='Natanael', last_name='Acosta')
        self.assertEqual(str(patient), self.patient.full_name)

    def test_patient_list_view(self):
        response = self.client.get(reverse('list_patients'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Natanael Acosta')
        self.assertTemplateUsed(response, 'app/patients_list_view.html')
