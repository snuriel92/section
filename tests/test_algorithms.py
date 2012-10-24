#!/usr/bin/python
import unittest
import sys

# FIXME pretty sure this is a hack, but I don't know how python works
sys.path.append('..')

from algorithms import sort_fns

class TestAlgorithms(unittest.TestCase):
    # run the given list through all algorithms.
    # asserts that all the results are identical
    # returns one of the results (which one does not matter, since they are
    # identical)
    def run_all_algorithms(self, lst):
        def run_sort(sort_fn):
            copy = list(lst)
            sort_fn(copy)
            return copy
        results = map(run_sort, sort_fns.values())
        for result in results[1:]:
            self.assertEqual(results[0], result)
        return results[0]

    def test_empty(self):
        self.assertEqual([], self.run_all_algorithms([]))
    def test_one(self):
        self.assertEqual(['asdf'], self.run_all_algorithms(['asdf']))
    def test_two(self):
        self.assertEqual(['asdf', 'def'], self.run_all_algorithms(['def', 'asdf']))


if __name__ == "__main__":
    unittest.main()
