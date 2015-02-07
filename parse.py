##!/usr/bin/env python3
# adapted from http://stackoverflow.com/questions/5036605/how-to-export-a-mysql-database-to-json
import json

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()
SOUGHT_ATTRIBUTES = "post_date post_date_gmt post_content post_title ID".split()

class WordpressPost(object):

    def __init__(self, *args, **kwargs):
        for k, v in kwargs:
            setattr(self, k, v)

    def make_dict(self):
        return {attrib: getattr(self, attrib) for attrib in SOUGHT_ATTRIBUTES}


import sqlalchemy
metadata = sqlalchemy.MetaData()
wp_posts_table = sqlalchemy.Table('wp_posts', metadata,
        sqlalchemy.Column('ID', sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column('post_title', sqlalchemy.String(100)),
        sqlalchemy.Column('post_content', sqlalchemy.String(100)),
        sqlalchemy.Column('post_date', sqlalchemy.Date),
        sqlalchemy.Column('post_date_gmt', sqlalchemy.Date),
    )

# connect the database.  substitute the needed values.
engine = sqlalchemy.create_engine('mysql://vagrant:vagrant@localhost/ronocdh_openveins?charset=utf8')

# if needed, create the table:
metadata.create_all(engine)

# map the model to the table
import sqlalchemy.orm
sqlalchemy.orm.mapper(WordpressPost, wp_posts_table)

QUERY = 'SELECT * FROM wp_posts;'
wp_posts = list(engine.execute(QUERY))


# and lets make some json out of it:
import json

wp_posts_json = json.dumps(wp_posts)
