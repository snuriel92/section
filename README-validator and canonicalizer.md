section
=======
(Run `python can-and-validate.py -h` to see instructions for running 
  can-and-validate.py.)

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
** UrlTracker uses functions lessThan for <, greaterThan for >, and equals for =
   and compares the actual url (not the canonicalized version)
** Assume 0-based indexing for each url, each index in a url corresponds to a 
   character in the url. A url’s length is the number of characters it consists of.

There is a python script can-and-validate.py in our root directory that takes one
argument. The argument, -i, provides the input file name. 

The proper usage of our script is:
python sort.py -i INPUT_FILE


Using the files we provide, one working command would be:
      python can-and-validate.py -i sample_input.txt

This will read in every url (assuming each url is on its own line in the file)
and print out the original url in the file, whether it is a valid url, its
canonical form, whether the original url is unique (not repeated in the input 
file) and whether the canonical url is unique (no url in the input file gives
the same canonical form).
An example output for a file only containing 
"http://en.wikipedia.org/wiki/Sarah_Jane_Smith#Appearances" is:

Source: http://en.wikipedia.org/wiki/Sarah_Jane_Smith#Appearances
  Valid: True
  Canonical: http://en.wikipedia.org/wiki/Sarah_Jane_Smith
  Source unique: True
  Canonicalized URL unique: True
 
VALIDATION:
To check if a url is valid, you must create a UrlTracker object from the 
url (as a string) in question. Say you call it "ut"; you can then call 
ut.valid to check whether the url is valid or not. 

Valid URL Spec:

valid-url ::= protocol “//” domain [ “:” port ] “/” [ path ] [ “?” query ] [ fragment ]

protocol ::= ”[a-z][\w-]+:” // alphanum + ‘-’, starts with lowercase alpha

domain ::= “[a-zA-Z0-9.-]+[.][a-zA-Z]{2,4}” // if it looks like a domain, it is one
(The domain must contain a period to be valid)

port ::= “[0-9]{0-5}” // valid ports range 0-65535

path ::= “[^\s()<>?]+”

query ::= key-value-pair [ “&” query ] // any number of key-value pairs separated by “&”

key-value-pair ::= “[^\s&=]+=[^\s&=]+” // two non-space/’&’/’=’ separated by ‘=’

fragment ::= “#[^\s]” // no spaces, otherwise, anything goes

CANONICALIZATION:
To get the canonicalized url, you must create a UrlTracker object from the 
url (as a string) in question. Say you call it "ut"; you can then call 
ut.canonicalized to get the canonicalized url back. 

Changes

* Convert protocol to lowercase:
    ex: hTtP://google.com → http://google.com

* Remove empty query string (“?”) at the end of a query/url:
    ex: http://www.example.com/display? → http://www.example.com/display

* Remove fragment: remove any present pound sign as well as everything after it
    ex: http://www.example.com/display#lala → http://www.example.com/display

Sorting query parameters was taken out because it is not necessirily the same link
if the queries are re-ordered. As an experiment I went into Google and searched for
"Jane Smith Four" and "Four Jane Smith" and got different result orders (and some 
results completely different) which indicates that the query parameter order was
important.
