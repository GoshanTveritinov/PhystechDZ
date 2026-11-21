import random

def partition(a, low, high):
    pivot = a[random.randint(low, high)]

    lt = low
    i = low
    gt = high

    while i <= gt:
        if a [i] < pivot:
            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1
        elif a[i] > pivot:
            a[gt], a[i] = a[i], a[gt]
            gt -= 1
        else:
            i += 1
    return lt, gt


def quickselct(a, k):
    def select(low, high):
        if low == high:
            return a[low]

        lt, gt = partition(a, low, high)

        if k < lt:
            return select(low, lt-1)

        elif k > gt:
            return select(gt+1, high)

        else:
            return a[k]

    return select(0, len(a)-1)


a = [7, 2, 9, 4, 1, 8, 3, 5, 6]
print(partition(a, 0, len(a)-1))

print(quickselct(a, 4))