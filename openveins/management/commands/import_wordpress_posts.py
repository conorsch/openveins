from django.core.management.base import NoArgsCommand, CommandError
from django.conf import settings
from openveins.models import Quote
import openveins
import os

import json
from pprint import pprint


class Command(NoArgsCommand):
    help = 'Imports Wordpress posts to Quote objects.'

    def handle_noargs(self, *args, **options):

        parent_dir = os.path.dirname(openveins.__file__)
        json_fixture_file = os.path.join(parent_dir, 'fixtures', 'wp_posts.json')

        wp_posts = json.load(open(json_fixture_file))
        for wp_post in wp_posts:
            print("Working on: ", end='')
            pprint(wp_post)
            try:
                Quote.objects.get(pk=wp_post['ID'])
            except Quote.DoesNotExist:
                quote = Quote.objects.create(
                    raw_text=wp_post.get('post_content'),
                    post_date=wp_post.get('post_date'),
                    pk=wp_post.get('ID'),
                )
                quote.save()
                self.stdout.write('Successfully imported quote titled "{}"'.format(wp_post.get('post_title')))
