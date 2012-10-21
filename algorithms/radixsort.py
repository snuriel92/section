# Radix sort

def sort(urls):
    temp = list(urls)
    maxlen = max(map(lambda url: len(url), temp))
    for i in range(maxlen, -1, -1):
      chars =  [[] for j in range (0, 256)] # Create a bucket for each char.
      for url in temp:
          # Grab the char or the 0 char if the string is ended.
          char = url[i] if i < len(url) else '\0'
          chars[ord(char)].append(url)
      temp = [item for sublist in chars for item in sublist] # flatten
    # Copy the values back into the original list.
    for i in range(0, len(urls)):
      urls[i] = temp[i]
    return urls
