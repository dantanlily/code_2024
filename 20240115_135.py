#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 10:31:30 2024

@author: dantan
"""

'''
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 

Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
'''

# In[]

ratings=[1,2,2,5,4,3,2]
ratings=[1,2,2]

def candy(ratings):
    candy=len(ratings)*[1]
    
    for i in range(1,len(ratings)):
        if ratings[i]>ratings[i-1]:
            candy[i]=candy[i-1]+1
        print(i,candy)
    for i in range(len(ratings)-2,-1,-1): # 3rd input in range is step gap
        if ratings[i]>ratings[i+1]:
            candy[i]=max(candy[i+1]+1,candy[i])
        print(i,candy[i])
    
    print(sum(candy))
            
        

# In[]
# think about starting from right and from left testing it in a bit longer array. 
from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy=len(ratings)*[1]
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                candy[i]=candy[i-1]+1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candy[i]=max(candy[i+1]+1,candy[i])
        return sum(candy)
    
s=Solution()
s.candy([1,2,2])
s.candy([1,2])
s.candy([1,0,2])
































