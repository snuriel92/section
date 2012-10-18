#!/usr/local/bin/python
"""
This script serves as the entry point for a simple sorting program
"""

import argparse
import sys

import algorithms

def main():
  parser = argparse.ArgumentParser(description='Simple sort program')

  parser.add_argument('-i', metavar='in-file', required=True,
                      type=argparse.FileType('r'),
                      help='Input file of strings to sort, one per line')
  parser.add_argument('-o', metavar='out-file', required=True,
                      type=argparse.FileType('w'),
                      help='Output file for sorted strings, one per line')
  parser.add_argument('--sort-fn', dest='sort_fn', default='insertion',
                      help='Sort function to use')

  results = parser.parse_args()
  infile = results.i
  outfile = results.o
  sort_fn = results.sort_fn

  try:
    lines = infile.readlines()
  except IOError, e:
    parser.error(str(e))
  finally:
    infile.close()
    infile = None

  lines = _sort(lines, sort_fn)

  try:
    for line in lines:
      outfile.write(line)
  except IOError, e:
    parser.error(str(e))
  finally:
    outfile.close()
    outfile = None

  sys.exit(0)

def _sort(str_list, sort_fn):
  """Return a sorted copy of str_list, using function sort_fn"""

  #TODO: actually sort and return
  return list(str_list)

if __name__ == '__main__':
  main()

