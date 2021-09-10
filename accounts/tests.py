from django.contrib.auth import authenticate, get_user_model
from django.test import TestCase, Client


class SigninTest(TestCase):

    def setUp(self):

        self.client = Client()

        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@gmail.com',
            password='test'
        )

        self.user.save()

        self.client.login(username='test', password='test')

    def test_correct(self):
        self.assertTrue(self.user.is_authenticated)
