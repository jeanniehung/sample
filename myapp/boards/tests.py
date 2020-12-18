from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .views import index, board_topics
from .models import Board
# Create your tests here.


class TestHome(TestCase):
    def setUp(self) -> None:
        Board.objects.create(name='Django', description='Django board.')

    def test_home_view_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_status_code(self):
        view = resolve('/')
        self.assertEqual(view.func, index)


class BoardTopicsTests(TestCase):
    def setUp(self) -> None:
        Board.objects.create(name='Django', description='Django board.')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    # def test_board_topics_view_not_found_status_code(self):
    #     url = reverse('board_topics', kwargs={'pk': 99})
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)








