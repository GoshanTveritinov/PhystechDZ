import heapq

m = int(input("Касс: "))
n = int(input("Клиенты: "))
l = list(map(int, input().split()))

if n != len(l):
    print("Колво клиентов и времен не совпадают")

heap = l[:m]
heapq.heapify(heap)

for time in l[:m]:
    free_time = heapq.heappop

print("Thats all")