"""
Link: https://www.geeksforgeeks.org/problems/help-a-thief5938/1
Help a Thief!!!
Difficulty: MediumAccuracy: 45.05%Submissions: 17K+Points: 4Average Time: 15m
You have to help a thief to steal as many as GoldCoins as possible from a GoldMine. There he saw N Gold Boxes an each Gold Boxes consists of Ai Plates each plates consists of Bi Gold Coins. Your task is to print the maximum gold coins theif can steal if he can take a maximum of T plates.

 

Example 1:

Input:
T = 3, N = 3 
A[] = {1, 2, 3}
B[] = {3, 2, 1}
Output:
7
Explanation:
The thief will take 1 plate of coins
from the first box and 2 plate of coins
from the second plate. 3 + 2*2 = 7. """

class Solution:
    def maxCoins(self, A, B, T, N):
        # code here
        arr = list(zip(B,A))
        arr.sort(reverse = True)
        
        loot = 0 
        for coin,plate in arr:
            if T == 0 :
                break
            
            taken = min(plate,T)
            
            loot += coin*taken
            T-=taken
        
        return loot