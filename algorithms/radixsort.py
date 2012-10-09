# Radix sort

def sort(urls):
    size = len(urls)
    maxlen = max(map(lambda url: len(url), urls))
    for i in range(maxlen, -1, -1):
      print i
      chars =  [[] for j in range (0, 256)] # Create a bucket for each char.
      for url in urls:
          # Grab the char or the 0 char if the string is ended.
          char = url[i] if i < len(url) else '\0'
          chars[ord(char)].append(url)
      urls = [item for sublist in chars for item in sublist] # flatten
    print urls
    return urls
