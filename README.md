section
=======
(Run `python sort.py -h` to see instructions for running sort.py.)

We chose to implement the sorting as follows.
* A character with a lower ASCII value comes before a character with a higher
  ASCII value. As a result, this means capitals take precedence over lowercase
  characters. This was chosen because parts of URLs are case sensitive and we
  felt it was important to respect that.
* If two strings start with the same character, the next character is used to
  break the tie (repeat as necessary)
* If looking at a character past the end of the string, it takes ASCII value 0
  (so if you have two strings with the first 5 characters the same, if the
  first string ends after character 5 and the second doesn't, the first string
  will alway come before the second in the output).

We have a python script sort.py in our root directory that takes three
arguments. The first argument, -i, provides the input file name. The second
argument, -o, provides the output file name, and --sort-fn provides the
recommended sort function. We also have an algorithms module in this root
directory that contains all of the sorting algorithms in their own file.
Loading our module also loads all of the individual sorts and allows easy
separation of the files while still providing a simple interface.

The proper usage of our script is:
python sort.py -i INPUT_FILE -o OUTPUT_FILE
    --sort-fn [radixsort, radixsort2, mergesort, mergesort2, quicksort,
               heapsort, selectionsort, selectionsort2]

Using the files we provide, one working command would be:
      python sort.py -i test_input.txt -o output.txt --sort-fn mergesort
You can then test the correctness of the sorting by calling:
      diff test_output.txt output.txt

The output file is created at the path OUTPUT_FILE relative to the directory
from which the script was run. For example, in our sample command, it would be
located in the current working directory. If you run the script from ..
relative to the sort.py script and provide -o other/directory/output.txt, it
will write the file to ../other/directory/output.txt relative to the sort.py
script.

Our choice for the O(n^2) algorithm was selection sort. We felt this was the
simplest algorithm to use and was very simple to implement in Python. For the
O(n log n) algorithms we included heapsort and mergesort, both of which have a
worst case runtime within the specified parameters. Python had built in
functions that made heapsort easy to use, and many of us have experience with
mergesort and quicksort, but we opted to use the former as quicksort would have
been much more complicated. The O(n) algorithm was radix sort, which uses
buckets for each possible ASCII value to sort the URLs. For all these
algorithms we assume that the URLs use proper ASCII values and do not contain
other symbols.


Group Division:
 * Corneliu, Brandon - Merge sort
 * Jeff- script setup and design.
 * Conor- radix sort 
 * Janette-  Heapsort
 * Nat- testing 
 * Shahaf- Selection sort
 * Shahaf & Janette- coordination   
