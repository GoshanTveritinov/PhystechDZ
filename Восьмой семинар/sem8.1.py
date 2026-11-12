import heapq

n, k = map(int, input().split())
line = list(map(int, input().split()))
kline = line[:k]
heap = [-i for i in line[:k]]
heapq.heapify(heap)
for i in kline:
    if i < -heap[0]:
        heapq.heapreplace(heap, -1)




print(*sorted (-i for i in heap))