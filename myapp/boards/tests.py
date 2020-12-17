from django.utils import timezone
from django.urls import reverse, resolve
from django.test import TestCase
from .models import Question
from boards import views

# Create your tests here.

class TestHome(TestCase):

    def setUp(self):
        Question.objects.create(question_text='question_text', pub_date=timezone.now())

    def test_home_view_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_status_code(self):
        view = resolve('/index/')
        self.assertEqual(view.func, views.index)




