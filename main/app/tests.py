from django.urls import resolve
from django.test import TestCase
from django.test import client
from django.urls import reverse
from app import views
from .models import Board

# Create your tests here.


class IndexTest(TestCase):

    def test_index_view_status_code(self):
        '''
        In [1]: from django.urls import reverse

        In [2]: reverse('app-index')
        Out[2]: '/index/'

        '''
        # url = reverse(views.index)  # url(r'^index/$', app.index, name='app-index'),
        url = reverse('app-index')
        c = client.Client()
        # response = c.get('/index/')
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/index/')  #ResolverMatch(func=app.views.index, args=(), kwargs={}, url_name=app-index, app_names=[], namespaces=[], route=^index/$)
        self.assertEqual(view.func, views.index)


class BoardTopicsTests(TestCase):

    def setUp(self) -> None:
        Board.objects.create(name='ZEGO', description='zegodescrptions')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        c = client.Client()
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_board_topics_url_resolves_home_view(self):
        view = resolve('/boards/1/')
        self.assertEqual(view.func, views.board_topics)


