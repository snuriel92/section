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
    return True
  def canonicalize(self, url):
    poundIdx = url.find("#")  
    if (poundIdx > -1):
      url = url[0:poundIdx]
    tmp = urlparse.urlsplit(url)
    return tmp.geturl()


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

  i = 0;  '''to keep track of index/number or lines'''
  urlarr = []
  
  for line in lines:
    line = line[0:len(line)-1]
    urlarr.append(UrlTracker(line))
    print "Source: " + urlarr[i].url
    print urlarr[i].valid
    print "Canonical: " + urlarr[i].canonicalized
    i += 1
  
if __name__ == '__main__':
  main()
