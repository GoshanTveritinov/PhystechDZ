def merge(left, right):
    ...

def merge_sort(array):
    if len (array) < 2:
        return array
    midpoint = len(array)//2
    return merge(merge_sort(array[:midpoint]), merge_sort(array[midpoint:]))

def quick_sort(array):
    ...