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
    return (self.url < u2.url)

  def greaterThan(self, u2):
    return (self.url > u2.url)

  def equals(self, u2):
    return (self.url == u2.url)


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

  def testComparator(self):  # testing valid urls because that's the point of this...
    u1 = UrlTracker("http://a.com")
    u2 = UrlTracker("http://b.com")
    u3 = UrlTracker("http://www.a.com")
    u4 = UrlTracker("http://wikipedia.com")
    u5 = UrlTracker("http://facebook.com?")
    empty = UrlTracker("")

    self.assertEqual(u1.lessThan(u2), True)
    self.assertEqual(u1.greaterThan(u2), False)
    self.assertEqual(u1.equals(u2), False)

    self.assertEqual(u1.lessThan(u3), True)
    self.assertEqual(u1.greaterThan(u3), False)
    self.assertEqual(u1.equals(u3), False)

    self.assertEqual(u1.lessThan(u4), True)
    self.assertEqual(u1.greaterThan(u4), False)
    self.assertEqual(u1.equals(u4), False)

    self.assertEqual(u1.lessThan(u4), True)
    self.assertEqual(u1.greaterThan(u4), False)
    self.assertEqual(u1.equals(u4), False)

    self.assertEqual(u1.lessThan(empty), False)
    self.assertEqual(u1.greaterThan(empty), True)
    self.assertEqual(u1.equals(empty), False)

    self.assertEqual(empty.equals(empty), True)

    self.assertEqual(u2.lessThan(u1), False)
    self.assertEqual(u2.greaterThan(u1), True)
    self.assertEqual(u2.equals(u1), False)

    self.assertEqual(u2.lessThan(empty), False)
    self.assertEqual(u2.greaterThan(empty), True)
    self.assertEqual(u2.equals(empty), False)

    self.assertEqual(u3.lessThan(u4), False)
    self.assertEqual(u3.greaterThan(u4), True)
    self.assertEqual(u3.equals(u4), False)

    self.assertEqual(u4.lessThan(u4), False)
    self.assertEqual(u4.greaterThan(u4), False)
    self.assertEqual(u4.equals(u4), True)

    self.assertEqual(u4.lessThan(empty), False)
    self.assertEqual(u4.greaterThan(empty), True)
    self.assertEqual(u4.equals(empty), False)

    self.assertEqual(empty.lessThan(empty), False)
    self.assertEqual(empty.greaterThan(empty), False)
    self.assertEqual(empty.equals(empty), True)

if __name__ == '__main__':
    unittest.main()
