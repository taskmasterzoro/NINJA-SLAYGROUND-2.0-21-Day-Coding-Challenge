"""Problem statement
You have been given an array ‘a’ of ‘n’ non-negative integers.You have to check whether the given array is sorted in the non-decreasing order or not.
Your task is to return 1 if the given array is sorted. Else, return 0.
Example :
Input: ‘n’ = 5, ‘a’ = [1, 2, 3, 4, 5]
Output: 1
The given array is sorted in non-decreasing order; hence the answer will be 1. """
def isSorted(n: int, a: [int]) -> int:
    # Iterate through the array starting from index 1
    for i in range(1, n):
        # If any element is smaller than the previous one, return 0
        if a[i] < a[i - 1]:
            return 0
    # If loop completes, the array is sorted, return 1
    return 1
