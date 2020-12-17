from django.test import TestCase
from django.urls import reverse, resolve
# from django.test import client
from .models import Board
from boards import views
# Create your tests here.

class TestHome(TestCase):
    def __str__(self):
        Board.objects.create(name='Js', description='this is js')

    def test_home_view_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_home_url_status_code(self):
        view = resolve('/')
        self.assertEqual(view.func, views.index)