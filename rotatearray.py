""" 
Link : https://www.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1
Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

Note: Consider the array as circular.

Examples :

Input: arr[] = [1, 2, 3, 4, 5], d = 2
Output: [3, 4, 5, 1, 2]
Explanation: when rotated by 2 elements, it becomes 3 4 5 1 2. """

class Solution:
    def reverse(self, arr, left , right):
        while left < right:
            arr[left],arr[right] = arr[right],arr[left]
            left+=1
            right-=1
        
    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        d = d%n
        self.reverse(arr,0,d-1)
        self.reverse(arr,d,n-1)
        self.reverse(arr,0,n-1)
        
        return arr
    