from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test import Client
from django.contrib.auth.hashers import make_password
from .factories import UserFactory
from django.contrib.auth import get_user_model


class TestUserPermissions(TestCase):

    def setUp(self):
        self.c = Client()
        self.pw = make_password('!')
        User = get_user_model()
        self.user = User.objects.create_user(username='fakeuser1', password=self.pw)

    def test_user_is_staff(self):
        self.assertTrue(self.user.is_staff)

    def test_user_is_logged_in(self):
        print("TRYING TO LOGIN...")
        print("USERNAME: '{}'".format(self.user.username))
        print("PASSWORD: '{}'".format(self.user.password))
        self.assertTrue(self.client.login(username=self.user.username, password=self.pw))

    def test_user_in_request_context(self):
        self.assertTrue(self.client.login(username=self.user.username, password=self.pw))
        response = self.c.get(reverse("home"), REMOTE_USER=self.user.username)
        user = response.context['user']
        self.assertFalse(user.is_anonymous())
        self.assertTrue(user.is_staff)
        self.assertEqual(response.status_code, 200)
