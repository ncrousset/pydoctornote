from django.http import response
from django.test import TestCase, SimpleTestCase, Client
from django.contrib.auth import authenticate, get_user_model
from django.urls import reverse

from app.models import Patient

from app.forms import PatientForm

from datetime import date


class PatientTest(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@gmail.com',
            password='test'
        )

        self.client = Client()
        self.client.login(username='testuser', password='test')

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

    def test_user_can_create_patient(self):
        data = {'first_name': 'Test', 'last_name': 'Test Last', 'sex': 'o'}

        form = PatientForm(data)
        response = self.client.post(reverse('create_patient'), data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Patient.objects.last().first_name, 'Test')
        self.assertEqual(Patient.objects.last().last_name, 'Test Last')

    def test_all_fields_were_saved_well(self):
        data = {
            'first_name': 'Pedro',
            'last_name': 'Lopez',
            'birth_date': '2001-02-15',
            'email': 'estephany@gmail.com',
            'insurance': '121542',
            'idd': '45545',
            'phone': '80954855',
            'sex': 'm',
            'next_appointment': '2021-11-20'
        }

        form = PatientForm(data)
        response = self.client.post(reverse('create_patient'), data)

        """ Get the last patient"""
        patient = Patient.objects.last()

        self.assertEqual(patient.first_name, 'Pedro')
        self.assertEqual(patient.last_name, 'Lopez')
        self.assertEqual(patient.birth_date, date.fromisoformat('2001-02-15'))
        self.assertEqual(patient.email, 'estephany@gmail.com')
        self.assertEqual(patient.insurance, '121542')
        self.assertEqual(patient.idd, '45545')
        self.assertEqual(patient.phone, '80954855')
        self.assertEqual(patient.sex, 'm')
        self.assertEqual(patient.next_appointment,
                         date.fromisoformat('2021-11-20'))

        """ This field was added with the session user """
        self.assertEqual(patient.user_id, self.user)

    def test_patient_list_view(self):
        response = self.client.get(reverse('list_patients'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Natanael Acosta')
        self.assertTemplateUsed(response, 'app/patients_list_view.html')

    def test_patient_detail_view(self):
        response = self.client.get(
            reverse('detail_patient', kwargs={"pk": self.patient.id}))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'app/patient_view.html')

    def test_user_can_see_the_fields_of_patient(self):
        response = self.client.get(
            reverse('detail_patient', kwargs={"pk": self.patient.id}))

        self.assertContains(response, self.patient.full_name)
        self.assertContains(response, self.patient.first_name)
        self.assertContains(response, self.patient.last_name)
        self.assertContains(response, self.patient.email)
        self.assertContains(response, self.patient.insurance)
        self.assertContains(response, self.patient.idd)
        self.assertContains(response, self.patient.phone)
        self.assertContains(response, self.patient.sex_title)
