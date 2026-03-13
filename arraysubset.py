"""
Link : https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1
Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

Examples:

Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
Output: true
Explanation: b[] is a subset of a[]
Input: a[] = [1, 2, 3, 4, 4, 5, 6], b[] = [1, 2, 4]
Output: true
Explanation: b[] is a subset of a[]
Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
Output: false
Explanation: b[] is not a subset of a[] """

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        freq = dict()
        
        for item in a:
            count = freq.get(item,0)
            freq[item] = count + 1
            
        for num in b:
            if num not in freq or freq[num] == 0 :
                return False
            freq[num]-=1
        
        return True