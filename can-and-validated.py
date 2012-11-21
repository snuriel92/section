#!/usr/local/bin/python
"""
This script serves as the entry point for a url canonicalization and
validation program
"""

import argparse
import sys
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


def main():
  parser = argparse.ArgumentParser(description=('URL canonocalization and'
      + ' validation program'))

  parser.add_argument('-i', metavar='in-file', required=True,
                      type=argparse.FileType('r'),
                      help=('input file of strings to validates and canonicalize,'
                       + ' one per line'))

  # Read parsed arguments
  results          = parser.parse_args()
  infile           = results.i

  # read lines
  try:
    lines = infile.readlines()
  except IOError, e:
    parser.error(str(e))
  finally:
    infile.close()
    infile = None

  i = 0  #to keep track of index/number or lines
  urlarr = []
  urldict = dict()  # maps urls to bools--> true if url is unique, false if not
  canondict = dict()

  for line in lines:
    if(line != '\n'):
      line = line[0:len(line)-1]  #remove the newline
      urlarr.append(UrlTracker(line))

      if(urlarr[i].url in urldict):
        urldict[urlarr[i].url] = False  # seen before so not unique
      else:
        urldict[urlarr[i].url] = True  # first time seen so unique

      if(urlarr[i].canonicalized in canondict):
        canondict[urlarr[i].canonicalized] = False  # seen before so not unique
      else:
        canondict[urlarr[i].canonicalized] = True  # first time seen so unique

      i += 1

  for u in urlarr:
    print "Source: " + u.url
    print "  Valid: " + printBool(u.valid)
    print "  Canonical: " + u.canonicalized
    print "  Source unique: " + printBool(urldict[u.url])
    print ("  Canonicalized URL unique: " 
           + printBool(canondict[u.canonicalized]))

def printBool(b):
  if b:
    return "True"
  else:
    return "False"

if __name__ == '__main__':
  main()
