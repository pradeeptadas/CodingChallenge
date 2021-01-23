#!/bin/python3

import math
import os
import random
import re
import sys
import operator
import copy

# Complete the minimumBribes function below.
def minimumBribesWrongFirst(q):
    adjusted_numbers = [(num - (i+1)) for i, num in enumerate(q)]

    if any(num>2 for num in adjusted_numbers):
        print ("Too chaotic")
    else:
        print(sum([abs(_) for _ in adjusted_numbers])//2)
 
def adjust_number(l, q):
    arr = []
    for i, k in zip(l, q):
        if i == k:
            arr.append(0)
        else:
            arr.append(l.index(k) - q.index(k))
    return arr


def update_l(l, empty_list):
    arr = copy.deepcopy(l)
    for i, k in enumerate(empty_list):
        if k !=0:
            arr[i] = l[i+k]
    return arr

def evolute(l, q):
    if (l == q):
        return 0
    count = 0
    
    adjusted_numbers = adjust_number(l, q)
    if any(num>2 for num in adjusted_numbers):
        return None
    empty_list = []
    for num in adjusted_numbers:
        if num == 0:
            empty_list.append(0)
        elif num > 0:
            count = count + num
            empty_list.append(num)
            for i in range(num):
                empty_list.append(-1)
            break
    
    if not empty_list:
        return count        
    else:
        for i in range(len(l)-len(empty_list)):
            empty_list.append(0)
    updated_l = update_l(l, empty_list)
    recurse_count = evolute(updated_l, q)
    if recurse_count is not None:
        count = count + recurse_count
    else:
        return None
    return count

def minimumBribesInefficient(q):
    l = len(q)
    count = evolute([i+1 for i in range(l)], q)
    if count:
        print(count)
    else:
        print("Too chaotic")

###################
## Actual Answer
###################
def minimumBribes(q):
    moves = 0 
    q = [i-1 for i in q]

    # Loop through each person (P) in the queue (Q)
    for i, num in enumerate(q):
        if num - i > 2:
            print("Too chaotic")
            return
        # count how many times num has RECEIVED a bribe, by looking at who is
        # ahead of num.  

        for j in range(max(num-1, 0), i):
            if q[j] > num:
                moves += 1
    print(moves)
    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)
