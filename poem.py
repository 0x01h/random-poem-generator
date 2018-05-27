#!/usr/bin/env python3

import random
import json
import urllib.request
import urllib.parse

def random_poem():
    contents = urllib.request.urlopen("http://poetrydb.org/title").read()
    readable = contents.decode('utf-8')

    data = json.loads(readable)

    poemUrl = "http://poetrydb.org/title/" + urllib.parse.quote((data['titles'][random.randint(0,2971)]), safe=':/?*=\'')

    contents = urllib.request.urlopen(poemUrl).read()
    readable = contents.decode('utf-8')

    data = json.loads(readable)

    title = data[0]['title']
    author = data[0]['author']
    lines = data[0]['lines']
    poem = ""

    print (title)
    print (author)
    for i in range(0,len(lines)):
        poem = poem + (lines[i]) + " \n"
    print (poem)

    return data

random_poem()
