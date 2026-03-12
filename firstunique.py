''' 
LInk : https://www.geeksforgeeks.org/problems/non-repeating-element3958/1
Find the first non-repeating element in a given array arr of integers and if there is not present any non-repeating element then return 0

Examples:

Input: arr[] = [-1, 2, -1, 3, 2]
Output: 3
Explanation: -1 and 2 are repeating whereas 3 is the only number occuring once. Hence, the output is 3. '''

#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr): 
        # Complete the function
        freq_arr = dict()
        for i in arr:
            count = freq_arr.get(i,0)
            freq_arr[i]= count+1
        
        for item in arr:
            unique = freq_arr.get(item,0)
            if unique == 1 :
                return item 
            
        return 0 
        