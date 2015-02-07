from django.core.management.base import NoArgsCommand
from openveins.models import Quote
from bs4 import BeautifulSoup
from pprint import pprint


class Command(NoArgsCommand):
    help = 'Parses imported Quote objects to populate fields.'

    def handle_noargs(self, *args, **options):

        quotes = Quote.objects.all()
        for quote in quotes:
            if quote.raw_text:
                quote = self.parse_raw_text(quote)
                if quote:
                    quote.save()

    def parse_raw_text(self, quote):

        soup = BeautifulSoup(quote.raw_text)
        text = soup.find('h3').text
        attribution = soup.find('p').text
        try:
            author, source, year = attribution.split('\r\n')
        except ValueError:
            print("Could not parse!")
            pprint(quote)
            return

        quote.author = author.lstrip('—').strip()
        quote.source = source.strip()
        quote.year = year.strip()
        quote.text = text
        return quote
