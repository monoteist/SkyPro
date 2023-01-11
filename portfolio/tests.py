from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from portfolio.models import Education, Experience, Speciality, Portfolio
from users.models import User


class ResumeTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='monoteist',
                                        password='passtest123')
        Education.objects.create(user=self.user, title='education')
        Experience.objects.create(user=self.user, title='expirience')
        Speciality.objects.create(user=self.user, title='speciality')
        Portfolio.objects.create(user=self.user, title='portfolio')

    def test_get_users(self):
        response = self.client.get(reverse('resume'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_patch_user(self):
        self.client.login(username='monoteist', password='passtest123')
        response = self.client.patch(reverse('resume'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)

    def test_patch_user_error(self):
        response = self.client.patch(reverse('resume'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)