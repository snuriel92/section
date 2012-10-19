#!/usr/local/bin/python
"""
This script serves as the entry point for a simple sorting program
"""

import argparse
import sys

from algorithms import sort_fns

def main():
  parser = argparse.ArgumentParser(description='Simple sort program')

  parser.add_argument('-i', metavar='in-file', required=True,
                      type=argparse.FileType('r'),
                      help='input file of strings to sort, one per line')
  parser.add_argument('-o', metavar='out-file', required=True,
                      type=argparse.FileType('w'),
                      help='output file for sorted strings, one per line')

  # get available sort functions to use for argument choices
  choices = tuple(sort_fns.keys())
  if 'selectionsort' in sort_fns:
    default = 'selectionsort'
  else:
    default = choices[0]

  parser.add_argument('--sort-fn', dest='sort_fn', choices=choices,
                      default=default,
                      help='sort function to use')

  results = parser.parse_args()
  infile = results.i
  outfile = results.o
  sort_fn = results.sort_fn

  # read lines
  try:
    lines = infile.readlines()
  except IOError, e:
    parser.error(str(e))
  finally:
    infile.close()
    infile = None

  # argparser guarantees a valid choice for sort_fn
  lines = _sort(lines, sort_fns[sort_fn].sort)

  # write output
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
  """Return a sorted copy of str_list, using functionsort_fn"""
  copy = list(str_list)

  sort_fn(copy)

  return copy

if __name__ == '__main__':
  main()

