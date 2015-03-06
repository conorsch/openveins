from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test import Client
from .factories import UserFactory, DEFAULT_PASSWORD


class TestUserPermissions(TestCase):

    def setUp(self):
        self.c = Client()
        self.pw = '!'
        self.user = UserFactory()

    def test_user_is_staff(self):
        self.assertTrue(self.user.is_staff)
        self.assertTrue(self.user.is_authenticated())
        self.assertFalse(self.user.is_anonymous())

    def test_user_can_login(self):
        self.assertTrue(self.client.login(username=self.user.username, password=DEFAULT_PASSWORD))

    def test_user_in_request_context(self):
        self.assertTrue(self.client.login(username=self.user.username, password=DEFAULT_PASSWORD))
        response = self.c.get(reverse("home"))
        self.assertTrue(self.user.is_authenticated())
        self.assertTrue(self.user.is_staff)
        self.assertEqual(response.status_code, 200)
