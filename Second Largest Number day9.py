"""Problem statement
You have been given an array ‘a’ of ‘n’ unique non-negative integers.
Find the second largest and second smallest element from the array.
Return the two elements (second largest and second smallest) as another array of size 2."""
def getSecondOrderElements(n: int, a: [int]) -> [int]:
    # Initialize variables to store the largest and smallest elements
    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')
    
    for num in a:
        # Update largest and second largest
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
        
        # Update smallest and second smallest
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    
    return [second_largest, second_smallest]
