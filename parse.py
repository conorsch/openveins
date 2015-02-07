##!/usr/bin/env python3
# adapted from http://stackoverflow.com/questions/5036605/how-to-export-a-mysql-database-to-json
import json
import sqlalchemy
from pprint import pprint


# connect the database.  substitute the needed values.
engine = sqlalchemy.create_engine('mysql://vagrant:vagrant@localhost/ronocdh_openveins?charset=utf8')
QUERY = 'SELECT ID, post_title, post_content, post_date FROM wp_posts WHERE post_status="publish";'

wp_posts = engine.execute(QUERY)
wp_posts = [dict(p) for p in wp_posts]


for i, post in enumerate(wp_posts):
    post['post_date'] = str(post['post_date'])
    wp_posts[i] = post

wp_posts_json = json.dumps(wp_posts)

fixtures_file = 'openveins/fixtures/wp_posts.json'

with open(fixtures_file, 'w') as f:
    f.write(wp_posts_json)

j = json.load(open(fixtures_file))
pprint(j)
