import math

class Heap(list):
  def __init__(self, array):
    list.__init__(self, array)
    self.height = int(math.log(len(array), 2))
    self.heap_size = len(array)

def parent(i):
  return int(i/2)

def left(i):
  return 2*i + 1

def right(i):
  return 2*i + 2

def swap(a, i, j):
  a[i], a[j] = a[j], a[i]

def max_heapify(a, i):
  l, r = left(i), right(i)
  if l < a.heap_size and a[l] > a[i]:
    largest = l
  else:
    largest = i
  if r < a.heap_size and a[r] > a[largest]:
    largest = r
  if largest != i:
    swap(a, i, largest)
    max_heapify(a, largest)

def build_max_heap(a):
  a.heap_size = len(a)
  for i in range(int(len(a)/2), -1, -1):
    max_heapify(a, i)

def heap_sort(a):
  build_max_heap(a)
  for i in range(len(a) - 1, -1, -1):
    swap(a, 0, i)
    a.heap_size -= 1
    max_heapify(a, 0)

array = [4, 5, 9, 34, 12, 45, 9, 45, 12, 23, 8, 1, 35]
a = Heap(array)
heap_sort(a)
print(a)
