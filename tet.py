# -*- coding:utf-8 -*-
from __future__ import print_function
import random
import time

def quick_sort(arr, first, last):
    """ Quicksort
        Complexity: best O(n) avg O(n log(n)), worst O(N^2)
    """
    if first < last:
        pos = partition(arr, first, last)
        # Start our two recursive calls
        quick_sort(arr, first, pos-1)
        quick_sort(arr, pos+1, last)

def partition(arr, first, last):
    wall = first
    for pos in range(first, last):
        if arr[pos] < arr[last]: # last is the pivot
            arr[pos], arr[wall] = arr[wall], arr[pos]
            wall += 1
    arr[wall], arr[last] = arr[last], arr[wall]
    return wall


test_list = [random.randint(0, 1000) for _ in range(1000)]
print("=" * 40)
print("quick_sort")
print("[src]", test_list[:100])
tic = time.time()
quick_sort(test_list, 0, len(test_list)-1)
print("[tar]", test_list[:100])
print("Elapsing time: %0.5f s" % (time.time()-tic))