from django.core.management.base import NoArgsCommand, CommandError
from openveins.models import Quote

import json
from pprint import pprint


class Command(NoArgsCommand):
    help = 'Imports Wordpress posts to Quote objects.'

    def handle_noargs(self, *args, **options):

        json_fixture_field = '/home/conor/gits/openveins/openveins/fixtures/wp_posts.json'

        wp_posts = json.load(open(json_fixture_field))
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
