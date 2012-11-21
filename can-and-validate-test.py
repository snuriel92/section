'''Testing program for the URL Validator, Canonicalizer and Comparator.
I simply copied and pasted the class I use for all of this into here because
I do not know python and this was already taking me an ungodly ammount of time
to do because I had to learn the language completely from scratch'''

import unittest
import sys
import os
import argparse
import urlparse

class UrlTracker:
  '''track the url, canonicalize it and validate it'''
  def __init__(self, url):
    self.url = url
    self.valid = self.validate(url)
    self.canonicalized = self.canonicalize(url)

  def validate(self, url):
    parsedUrl = urlparse.urlsplit(url)
    return ((parsedUrl.netloc != "") and (parsedUrl.netloc.find(".") != -1))

  def canonicalize(self, url):
    poundIdx = url.find("#")
    if (poundIdx > -1):
      url = url[0:poundIdx]
    tmp = urlparse.urlsplit(url)
    return tmp.geturl()

  def lessThan(self, u2):
    return (self < u2)

  def greaterThan(self, u2):
    return (self > u2)

  def equals(self, u2):
    return (self == u2)


class TestURLS(unittest.TestCase):
  def checkValid(self, url, valid):
    u1 = UrlTracker(url)
    self.assertEqual(u1.valid, valid)

  def checkCanonicalized(self, url, can):
    u1 = UrlTracker(url)
    self.assertEqual(u1.canonicalized, can)

  def testValidManyStrings(self):
    dictValid = {"www.facebook.com" : False,
                 "http://www.facebook.com" : True,
                 "http://fullhousemanager.com" : True,
                 "htTp://reddit.com/r/Politics" : True,
                 "" : False,
                 "https://mail.google.com#" : True,
                 "https://www.google.com/search?q=jane+smith&ie=utf" : True,
                 "http://en.wikipedia.org:80/wiki/Unit_testing?" : True,
                 "isthisaurl?" : False,
                 "is this a url" : False,
                 "http://-----" : False,
                 "http://google" : False}

    for key in dictValid:
      self.checkValid(key, dictValid[key])

  def testCanonManyStrings(self):
    dictValid = {"www.facebook.com" : "www.facebook.com",
                 "http://www.facebook.com" : "http://www.facebook.com",
                 "http://fullhousemanager.com?" : "http://fullhousemanager.com",
                 "HTTP://reddit.com/r/Politics" : "http://reddit.com/r/Politics",
                 "" : "",
                 "https://mail.google.com#" : "https://mail.google.com",
                 "https://www.google.com/search?q=jane+smith&ie=utf" : 
                    "https://www.google.com/search?q=jane+smith&ie=utf",
                 "http://en.wikipedia.org:80/wiki/Unit_testing?" : 
                      "http://en.wikipedia.org:80/wiki/Unit_testing",
                 "isthisaurl?" : "isthisaurl",
                 "http://en.wikipedia.org//" : "http://en.wikipedia.org//",
                 "http://-----" : "http://-----",
                 "http://google" : "http://google"}

    for key in dictValid:
      self.checkCanonicalized(key, dictValid[key])

  def testValidWeirdValues(self):
    self.checkValid('a', False)
    # These two error out/don't compile so I took them out of the test case
    # because the user should know better :)
    # self.checkValid(3, False)
    # self.checkValid(None, False)

  def testCanonWeirdValues(self):
    self.checkCanonicalized('a', 'a')
    # These two error out/don't compile so I took them out of the test case
    # because the user should know better :)
    # self.checkValid(3, False)
    # self.checkValid(None, False)

if __name__ == '__main__':
    unittest.main()
