"""Mengurutkan array integer

    Fungsi
        sort(arr, ascending) -> [int]   :   mengurutkan dalam tempat, juga mengembalikan 
                                            array integer yang terurut
"""


def insertion_sort_asc(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1

        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    
    return arr

def insertion_sort_desc(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1

        while j>=0 and key > arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

    return arr

def sort(arr, ascending=True):
    if ascending:
        return insertion_sort_asc(arr)
    else:
        return insertion_sort_desc(arr)