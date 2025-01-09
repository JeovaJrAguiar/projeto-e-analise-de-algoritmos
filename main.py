import numpy as np
import time

def bubbleSort(arr):
    for n in range(len(arr)-1,0,-1):
        for i in range(n):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

def insertion_sort(arr):
    n = len(arr)

    for i in range(n):
        aux = arr[i]
        j = i-1

        while j >= 0 and arr[j] > aux:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = aux

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
    
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def insertion_quick_sort(arr, threshold=100):
    if len(arr) <= threshold:
        insertion_sort(arr)
        return arr
    else:
        quicksort(arr)
        return arr

# geracao de vetores
n_sizes = [10, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8]
#n_sizes = [10**5]


data = {}
rng = np.random.default_rng()

for n in n_sizes:
      data[n] = rng.integers(low=0, high=100, size=n)

# mensurando tempos
def measure_execution_time(func, arr):
    times = []
    for _ in range(10):
        temp = arr.copy()
        start = time.time()
        func(temp)
        end = time.time()
        times.append(end - start)
    return sum(times) / len(times)

for size, vector in data.items():
    if isinstance(vector, np.ndarray):
        # bubble
        avg_time = measure_execution_time(bubbleSort, vector)
        print(f"{bubbleSort.__name__}, {size}, Tempo médio: {avg_time:.10f} segundos")
        
        # insertion
        avg_time = measure_execution_time(insertion_sort, vector)
        print(f"{insertion_sort.__name__},  {size}, Tempo médio: {avg_time:.10f} segundos")
        
        # quicksort
        avg_time = measure_execution_time(quicksort, vector)
        print(f"{quicksort.__name__}, {size}, Tempo médio: {avg_time:.10f} segundos")
        
        # merge
        avg_time = measure_execution_time(mergeSort, vector)
        print(f"{mergeSort.__name__}, {size}, Tempo médio: {avg_time:.10f} segundos")

        # hibrido
        avg_time = measure_execution_time(insertion_quick_sort, vector)
        print(f"{insertion_quick_sort.__name__}, {size}, Tempo médio: {avg_time:.10f} segundos")
