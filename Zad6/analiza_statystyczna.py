import random
import time
from Bubblesort.bubblesort import *
from Countingsort.countingsort import *
from Heapsort.heapsort import *
from Mergesort.mergesort import *
from Quicksort.quicksort import *
from Shellsort.shellsort import *


def count_time(func):
    start_time = time.time()
    func()
    return f"sort in {(time.time() - start_time)} seconds"


def stats_of_sort(arr):
    print(str(len(arr)) + " elements \n")
    # print("bubble sort: "+count_time(lambda: bubble_sort(arr)))
    print("counting sort: "+count_time(lambda: counting_sort(arr)))
    print("heap sort: "+count_time(lambda: heap_sort(arr)))
    print("merge sort: "+count_time(lambda: merge_sort(arr)))
    print("quick sort: "+count_time(lambda: quick_sort(arr, 0, len(array10)-1)))
    print("shell sort: "+count_time(lambda: shell_sort(arr)))
    print("\n\n\n")


array10 = [random.randint(1, 100) for _ in range(10)]
stats_of_sort(array10)

array100 = [random.randint(1, 100) for _ in range(100)]
stats_of_sort(array100)

array500 = [random.randint(1, 100) for _ in range(500)]
stats_of_sort(array500)

array1000 = [random.randint(1, 100) for _ in range(1000)]
stats_of_sort(array1000)

array100000 = [random.randint(1, 100) for _ in range(100000)]
stats_of_sort(array100000)

array500000 = [random.randint(1, 100) for _ in range(500000)]
stats_of_sort(array500000)

array1000000 = [random.randint(1, 100) for _ in range(1000000)]
stats_of_sort(array1000000)