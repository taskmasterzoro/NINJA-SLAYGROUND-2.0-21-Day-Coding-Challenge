""" Problem statement
You are given a number 'n'.
Return number of digits in ‘n’.
Example:
Input: 'n' = 123
Output: 3
Explanation:
The 3 digits in ‘123’ are 1, 2 and 3. """
  import java.util.*;

public class Solution {
    public static int countDigits(int n) {
        // Convert the number to a string and count the length
        return String.valueOf(n).length();
    }

    // Main method for testing
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input the number
        System.out.print("Enter a number: ");
        int n = sc.nextInt();

        // Calculate and print the number of digits
        int result = countDigits(n);
        System.out.println("Number of digits: " + result);

        sc.close();
    }
}
