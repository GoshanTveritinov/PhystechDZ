class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)
        self.heapify()

    def left(self, i):
        if (2*i+1) < self.size:
            return self.arr[2*i+1]
        else:
            return None

    def right(self, i):
        if (2*i+2) < self.size:
            return self.arr[2*i+2]
        else:
            return None

    def parent(self,i):
        if ((i-1)//2) < 0:
            return None
        else:
            return self.arr[(i-1)//2]

    def SiftDown(self, value, i):
        right = self.right(i)
        left = self.left(i)
        if left is None and right is None:
            return
        if left is None:
            if value >= right:
                return
            else:
                self.arr[i] = right
                self.arr[2 * i + 2] = value
                self.SiftDown(value, 2 * i + 2)
        elif right is None:
            if value >= left:
                return
            else:
                self.arr[i] = left
                self.arr[2 * i + 1] = value
                self.SiftDown(value, 2 * i + 1)
        else:
            if value >= right and value >= left:
                return
            else:
                if right > left:
                    self.arr[i] = right
                    self.arr[2*i+2] = value
                    self.SiftDown(value, 2*i+2)
                else:
                    self.arr[i] = left
                    self.arr[2*i+1] = value
                    self.SiftDown(value, 2*i+1)

    def SiftUp(self, value, i):
        parent = self.parent(i)
        if parent is None:
            return
        if value > parent:
            self.arr[(i-1)//2] = value
            self.arr[i] = parent
            self.SiftUp(value, (i-1)//2)
        else:
            return

    def get_max(self):
        return self.arr[0]

    def append(self, value):
        self.arr.append(value)
        self.size += 1
        self.SiftUp(value, self.size-1)

    def pop(self):
        if self.size == 0:
            return
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        self.size-=1
        self.arr.pop()
        if self.size > 0:
          self.SiftDown(self.arr[0], 0)

    def heapify(self):
        index = (self.size - 2)//2
        for i in range(index, -1, -1):
            self.SiftDown(self.arr[i], i)

    def HeapSort(arr):
        ans = []
        h = Heap(arr)
        while h.size > 0:
            ans.append(h.get_max())
            h.pop()
        return ans