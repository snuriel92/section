# Heap sort
from heapq import heappush, heappop

def sort(urls):
    size = len(urls)
    heap = []
    for url in urls:
        heappush(heap, url)
        urls.pop(0)
    for i in range(size):
        urls.insert(0, heappop(heap))
    return
