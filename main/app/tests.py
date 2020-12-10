from django.urls import resolve
from django.test import TestCase
from django.test import client
from django.urls import reverse
from app import views
from .models import Board

# Create your tests here.


class IndexTest(TestCase):

    def setUp(self) -> None:
        self.board = Board.objects.create(name='kio', description='kiodescription')
        self.url = reverse('home')
        self.response = client.Client().get(self.url)

    def test_index_view_status_code(self):
        '''
        In [1]: from django.urls import reverse

        In [2]: reverse('app-index')
        Out[2]: '/index/'

        '''
        # url = reverse(views.index)  # url(r'^index/$', app.index, name='app-index'),
        # url = reverse('home')
        # c = client.Client()
        # response = c.get(url)  # /index/
        self.assertEqual(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')  #ResolverMatch(func=app.views.index, args=(), kwargs={}, url_name=app-index, app_names=[], namespaces=[], route=^index/$)
        self.assertEqual(view.func, views.home)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))


class BoardTopicsTests(TestCase):

    def setUp(self) -> None:
        Board.objects.create(name='ZEGO', description='zegodescrptions')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        c = client.Client()
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_board_topics_view_not_find_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        c = client.Client()
        response = c.get(url)
        self.assertEqual(response.status_code, 404)

    def test_board_topics_url_resolves_home_view(self):
        view = resolve('/boards/1/')
        self.assertEqual(view.func, views.board_topics)

    def test_board_topics_view_contains_link_back_to_homepage(self):
        board_topic_url = reverse('board_topics', kwargs={'pk': 1})
        response = client.Client().get(board_topic_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))


class NewTopicsTests(TestCase):

    def setUp(self) -> None:
        Board.objects.create(name='MK', description='MKdescrptions')

    def test_new_topic_view_success_status_code(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        response = client.Client().get(url)
        self.assertEqual(response.status_code, 200)

    def test_new_topic_view_not_found_status_code(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        response = client.Client().get(url)
        self.assertEqual(response.status_code, 200)

    def test_new_topics_url_resolves_home_view(self):
        view = resolve('/boards/1/new/')
        self.assertEqual(view.func, views.new_topic)

    def test_new_topics_view_contains_link_back_to_homepage(self):
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})
        response = client.Client().get(new_topic_url)
        board_topic_url = reverse('board_topics', kwargs={'pk': 1})
        self.assertContains(response, 'href="{0}"'.format(board_topic_url))

