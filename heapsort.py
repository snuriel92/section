# Heap sort

def sort(urls):
    size = len(urls)
    heap = []
    for url in urls:
        heappush(heap, url)
        urls.pop(0)
    for i in range(size):
        urls.append(heappop(heap))
    return
