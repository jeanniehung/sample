from django.urls import reverse
from django.test import TestCase
from django.test import client

# Create your tests here.


class IndexTest(TestCase):

    def test_index_view_status_code(self):
        c = client.Client()
        response = c.get('/index/')
        self.assertEqual(response.status_code, 200)



