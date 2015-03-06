from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from .factories import UserFactory, DEFAULT_PASSWORD


class TestPublicViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = None

    def test_home_page(self):
        # quotes should be visible
        response = self.client.get(reverse("home"), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_endless_pagination(self):
        # TODO: make sure JS adds Quote objects to DOM
        pass


class TestPrivateViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserFactory()

    def test_anonymous_user_cannot_add_new_quote(self):
        response = self.client.get(reverse("new-quote"), follow=True)
        self.assertEqual(response.status_code, 403)

    def test_authenticated_user_can_add_new_quote(self):
        self.assertTrue(self.client.login(username=self.user.username, password=DEFAULT_PASSWORD))
        response = self.client.get(reverse("new-quote"), follow=True)
        self.assertEqual(response.status_code, 200)
