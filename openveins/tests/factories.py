import factory
from factory import fuzzy
from django.contrib.auth import get_user_model
from openveins.models import Quote

import random


class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = get_user_model()
    username = factory.Sequence(lambda n: "fakeuser{0}".format(n))
    email = factory.LazyAttribute(lambda obj: "{0}@example.com".format(obj.username))
    is_staff = True
    is_active = True


class QuoteFactory(factory.DjangoModelFactory):
    class Meta:
        model = Quote

    text = factory.fuzzy.FuzzyText(length=100)
    author = factory.fuzzy.FuzzyText(length=10)
    source = factory.fuzzy.FuzzyText(length=10)

    @factory.lazy_attribute
    def editorial(self):
        if random.choice([True, False]):
            editorial = factory.fuzzy.FuzzyText(length=200)
        else:
            editorial = ''
        return editorial


