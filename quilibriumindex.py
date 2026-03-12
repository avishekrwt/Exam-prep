""" 
Link : https://www.geeksforgeeks.org/problems/equal-sum0810/1
Given an array arr. Determine if there exists an element in the array such that the sum of the elements on its left is equal to the sum of the elements on its right. If there are no elements to the left/right, then the sum is considered to be zero. 

Example:

Input: arr[] = [1, 2, 3, 3]
Output: true
Explanation: Consider 1-based indexing i = 3, for [1, 2] sum is 3 and for [3] sum is also 3.
Input: arr[] = [1, 5]
Output: false
Explanation: No such index present. """

#User function Template for python3
class Solution:
    def equilibrium(self,arr): 
        #Your code here
        sum_of_array = sum(arr)
        prefix_sum = 0 
        for i in range(len(arr)):
    	    suffsum = sum_of_array - prefix_sum - arr[i]
    	    if suffsum == prefix_sum :
    	        return 'true'
    	    prefix_sum += arr[i]
        
        return 'false'