/*problem statement
You are given an array 'arr' sorted in non-decreasing order and a number 'x'. You must return the index of the lower bound of 'x'.
Note:
1. For a sorted array 'arr', 'lower_bound' of a number 'x' is defined as the smallest index 
'idx' such that the value 'arr[idx]' is not less than 'x'.If all numbers are smaller than 'x', 
then 'n' should be the 'lower_bound' of 'x', where 'n' is the size of the array.
2. Try to do this in O(log(n)). */
public class Solution {
    public static int lowerBound(int[] arr, int n, int x) {
        // Initialize search bounds
        int left = 0, right = n;
        
        // Binary search for the lower bound
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] < x) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        return left;
    }
}
