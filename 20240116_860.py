#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 23:25:36 2024

@author: dantan
"""

'''
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

 

Example 1:

Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
Example 2:

Input: bills = [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.
 

Constraints:

1 <= bills.length <= 105
bills[i] is either 5, 10, or 20.
'''

# In[]

# 5 no need to change
# 10 need 5 to change
# 20 need 10, 5 or 5 ,5, 5 to change
# pay attention to if else position match


def lemonadeChange(bills):
    coin_5=0
    coin_10=0
    coin_20=0
    for coin in bills:
        
        if coin==5:
            coin_5+=1
        if coin==10:
            if coin_5>=1:
                coin_5-=1
                coin_10+=1
            else:
                return False
        if coin==20:
            if coin_10>=1 and coin_5>=1:
                coin_20+=1
                coin_10-=1 
                coin_5-=1 
            elif coin_5>=3:
                coin_5-=3
                coin_20+=1 
            else:
                return False
        #print(coin,coin_5,coin_10,coin_20)
    return True  

# In[]
bills=[5,5,5,10,20]
bills= [5,5,10,10,20]
lemonadeChange(bills)
    
# In[]
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        coin_5 = 0
        coin_10 = 0
        
        for bill in bills:
            if bill == 5:
                coin_5 += 1
            elif bill == 10:
                if coin_5 > 0:
                    coin_5 -= 1
                    coin_10 += 1
                else:
                    return False
            else:  # bill is 20
                if coin_10 > 0 and coin_5 > 0:
                    coin_10 -= 1
                    coin_5 -= 1
                elif coin_5 >= 3:
                    coin_5 -= 3
                else:
                    return False
        return True

# In[]
    
    
    
    
    
    
    
    
    
    
    
    
    
    