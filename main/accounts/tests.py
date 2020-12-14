from django.test import TestCase
from django.test import client
from django.urls import reverse
from django.urls import resolve
from accounts import views


# Create your tests here.
class TestSignUp(TestCase):
    def test_signup_success(self):
        url = reverse('signup')
        response = client.Client().get(url)
        self.assertEqual(response.status_code, 200)

    def test_signup_func(self):
        view = resolve('/signup/')
        self.assertEqual(view.func, views.signup)
