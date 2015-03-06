#!/usr/bin/env python
from django.test import TestCase, Client
from .factories import UserFactory
from django.contrib.auth import get_user_model


class TestUserFactoryAttributes(TestCase):

    def setUp(self):
        self.c = Client()
        self.user = UserFactory()
        self.user_model = get_user_model()

    def test_ensure_users_exist(self):
        self.assertTrue(self.user_model.objects.filter(username=self.user.username))
        self.assertTrue(self.user.is_authenticated())

        self.assertTrue(self.user_model.objects.filter(username=self.user.username))
        self.assertTrue(self.user.is_authenticated())

        self.assertFalse(self.user_model.objects.filter(username='xxxxxxxxxxx'))

    def test_create_user(self):
        u = UserFactory()
        self.assertTrue(u.email.startswith(u.username))
        self.assertTrue(u.is_staff)
        self.assertFalse(u.is_superuser)


