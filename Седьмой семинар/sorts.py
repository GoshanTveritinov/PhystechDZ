b = [70, 30, 20, 60, 10, 50, 40]


def bubble(a):
    for j in range(len(a)-1):

        for i in range(len(a)-j-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return(a)

#print(bubble (b))

def insertion(a):
    for i in range(1, len(a)):
        key_item = a[i]
        j = i-1
        while j >= 0 and a[j] > key_item:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key_item
    return a

#print(insertion (b))
def selection(a):
    for i in range (len(a)-1):
        min_index = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a.insert(i, a.pop(min_index))
    return a

#print(selection(b))




