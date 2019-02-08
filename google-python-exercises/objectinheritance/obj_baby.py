#!/usr/bin/python -tt

import urllib


def wget(url):
    try:
        text = urllib.urlopen(url)
        if text.info().gettype() == 'text/html':
            print text.read()
    except IOError:
        print " could not access web address ", url
        
wget('')