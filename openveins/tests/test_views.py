from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from openveins.models import Quote
from django.core.exceptions import ValidationError
from .factories import UserFactory, QuoteFactory


class TestViews(TestCase):

    def setUp(self):
        self.c = Client()
        self.user = UserFactory()

    def test_home_page(self):
        # quotes should be visible
        response = self.c.get(reverse("home"))
        self.assertFalse('<div class="container quote-box">' in str(response.content))
