""" Problem statement
You have been given an array/list 'arr' consisting of 'n' elements.
Each element in the array is either 0, 1 or 2.
Sort this array/list in increasing order.
Do not make a new array/list. Make changes in the given array/list."""

from typing import List

def sortArray(arr: List[int], n: int) -> None:
    # Initialize pointers
    low, mid, high = 0, 0, n - 1
    
    while mid <= high:
        if arr[mid] == 0:
            # Swap arr[mid] with arr[low]
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            # Leave 1 in place and move the mid pointer
            mid += 1
        else:  # arr[mid] == 2
            # Swap arr[mid] with arr[high]
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
