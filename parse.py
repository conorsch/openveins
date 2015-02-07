#!/usr/bin/env python3
import json
import codecs


filename = "wp_posts.json"

f = codecs.open(filename, 'r', 'utf-8')
s = f.read()
s = s.replace('\r', '\\r').replace('\n', '\\n')
s = s.replace('\r', '\\r').replace('\n', '\\n')

print("Char 656 is: '{}'".format(s[656]))


json.loads(s)
