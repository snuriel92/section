import heapsort
import radixsort
import selectionsort
import mergesort
import url_validation
import other_sort_algorithms as other

def wrapper(sort_fn):
  def f(elements):
    ret = sort_fn(elements)
    elements[0:] = ret
  return f

# Sort function names to the function references
sort_fns = {
  'selectionsort': selectionsort.sort,
  'heapsort': heapsort.sort,
  'radixsort': radixsort.sort,
  'mergesort': mergesort.sort,
  'quicksort': wrapper(other.quicksort),
  'mergesort2': wrapper(other.mergesort),
  'radixsort2': wrapper(other.radixsort),
  'selectionsort2': wrapper(other.selectionsort),
}

# URL validation options to function references 
url_validation_fns = {
  'all':     url_validation.all,
  'valid':   url_validation.valid,
  'invalid': url_validation.invalid,
}
