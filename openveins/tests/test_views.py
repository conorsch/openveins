from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from openveins.models import Quote
from django.core.exceptions import ValidationError
from .factories import UserFactory, QuoteFactory


class TestPublicViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = None

    def test_home_page(self):
        # quotes should be visible
        response = self.client.get(reverse("home"))
        print("PUBLIC VIEW CONTENT:")
        print(response.content)

        self.assertTrue('<div class="container quote-box">' in str(response.content))

class TestPrivateViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserFactory()

    def test_home_page(self):
        # quotes should be visible
        response = self.client.get(reverse("home"))
        self.assertTrue('<div class="container quote-box">' in str(response.content))
