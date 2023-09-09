def selectionSort(List):
    for i in range(len(List)):
        min_index = i
        for j in range(i + 1, len(List)):
            if List[j] < List[min_index]:
                min_index = j
        List[i], List[min_index] = List[min_index], List[i]


def bubbleSort(List):
    for i in range (0, len(List)):
        for j in range (0, len(List)-i-1):
            if List[j] > List [j + 1]:
                List[j], List[j + 1] = List[j + 1], List[j]


def insertionSort(List):
    for i in range(1, len(List)):
        key = List[i]
        j = i-1
        while j >=0 and key < List[j]:
            List[j+1] = List[j]
            j -= 1
        List[j+1] = key


def heapify(List, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and List[i] < List[l]:
        largest = l
    if r < n and List[largest] < List[r]:
        largest = r
    if largest != i:
        List[i], List[largest] = List[largest], List[i]
        heapify(List, n, largest)
 
  
def heapSort(List):
    n = len(List)
    for i in range(n // 2 - 1, -1, -1):
        heapify(List, n, i)
    for i in range(n - 1, 0, -1):
        (List[i], List[0]) = (List[0], List[i])
        heapify(List, i, 0)
