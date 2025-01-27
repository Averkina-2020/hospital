from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User

from .models import Patient

from rest_framework_simplejwt.tokens import RefreshToken


class PatientAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.doctor_user = User.objects.create_user(
            username='doctor_user',
            password='password123'
        )
        self.doctor_user.role = 'doctor'
        self.doctor_user.save()
        self.nondoctor_user = User.objects.create_user(
            username='nondoctor_user',
            password='password123'
        )
        self.nondoctor_user.role = 'not_doctor'
        self.nondoctor_user.save()

        self.patient1 = Patient.objects.create(
            date_of_birth='1990-01-01',
            diagnoses=["Diagnosis 1", "Diagnosis 2"]
        )
        self.patient2 = Patient.objects.create(
            date_of_birth='1985-05-05',
            diagnoses=["Diagnosis 3"]
        )

    def test_login(self):
        response = self.client.post('/api/login/', {
            'username': 'doctor_user',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_get_patients_as_doctor(self):
        # Получение JWT токена для доктора
        refresh = RefreshToken.for_user(self.doctor_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.get('/api/patients/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_patients_as_nondoctor(self):
        # Получение JWT токена для не доктора
        refresh = RefreshToken.for_user(self.nondoctor_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.get('/api/patients/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_patients_without_auth(self):
        # Если пользователь не авторизован
        response = self.client.get('/api/patients/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
