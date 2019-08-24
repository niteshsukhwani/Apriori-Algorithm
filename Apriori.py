#!/usr/bin/env python
# coding: utf-8

#  Created By : Nitesh Sukhwani
#  Algorith Name : Apriori Algorithm 
#  Work : Finding Frequenent set and associated rule

'''Loading Required Library'''

import numpy as np
import copy as cp
import itertools

"""
filename = name of the file in which transaction data is given
c1 = generate dictionary of individual items with there corresponding frequency
l = total number of transaction
"""

def candidate1(filename):
    f= open(filename,"r")
    c1 ={}
    l = 0
    for line in f.readlines():
        l+=1
        line = line.strip()
        line =line.replace('"','')
        lst = line.split(',')
        for item in lst:
            count = c1.get(item,0)
            c1[item] = count+1
    return c1,l

"""
cand = dictionary of itemset with corresponding frequency as value
n = total number of transaction
support = minimum support for a item to be frequenct
l = list of items which are frequent
"""

def freq(cand,n,support):
    l = []
    for item in cand:
        x = cand[item]/n
        if x >= support:
            l.append(item)
    return l

'''
s = list of item
n = length of combination set
lst = a list of item give the subset of length n
'''

def findsubsets(s, n): 
    lst = []
    for i in itertools.combinations(s, n):
        lst.append(frozenset(i))
    return lst

"""
lk = lst of all frequenent itemset of length k
ele = an item of lenght k+1
return True if all subset of ele are present in lk
"""

def pruning(lk,ele):
    k = len(ele)-1
    subset = findsubsets(ele,k)
    for i in subset:
        if i not in lk:
            return False
    return True

"""
lk1 = frequent itemset of length k
lk2 = candidates for length k=1
"""

def gen_cand(lk1):
    lk = cp.deepcopy(lk1)
    n = len(lk)
    lk2 = []
    k = len(lk[0])
    for i in range(n-1):
        lkt1 = list(lk[i])
        for j in range(i+1,n):
            lkt2 = list(lk[j])
            flag =True
            for l in range(k-1):
                if lkt1[l]!=lkt2[l]:
                    flag =False
            if flag:
                lst = cp.deepcopy(lkt1)
                lst.append(lkt2[k-1])
                lst = frozenset(lst)
                if pruning(lk,lst):
                    lk2.append(lst)
    return lk2
                
"""
filename = name of the file in which transaction data is given
lk1 = candidate itemset of length k
c = Return dictionary of frequency of each candidate itemset in lk1
"""

def get_candidate(filename,lk1):
    lk = cp.deepcopy(lk1)
    f = open(filename,"r")
    c ={}
    l = 0
    k = len(lk[0])
    for line in f.readlines():
        l+=1
        line = line.strip()
        line =line.replace('"','')
        lst = line.split(',')
        subset = findsubsets(lst,k)
        for i in lk:
            #i_t = tuple(i)
            if i in subset:
                count = c.get(i,0)
                c[i]=count+1
    return c

"""
filename = name of the file in which transaction data is given
support = minimum support at which frequenent items are considered
freq_set = frequent itemset which have frequency greater than support 
"""

def apriori(filename,support=0.35):
    freq_set = []
    cand1,n = candidate1('GroceryStoreDataSet.csv')
    l1 = freq(cand1,n,support)
    for i in l1:
        freq_set.append(frozenset({i}))
    c2 = findsubsets(l1,2)
    while len(c2)!=0:
        cand = get_candidate(filename,c2)
        l2 = freq(cand,n,support)
        if len(l2)==0:
            break
        for i in l2:
            freq_set.append(i)
        c2 = gen_cand(l2)
    return freq_set

"""
freq_set : a dictionary conatining frequent set with corresponding freq
confidence : confidence value
Rule : dictionary giving association rules
"""

def rules(freq_set,confidence=0.56):
    Rule = {}
    for key in freq_set.keys():
        if len(key)==1:
            continue
        k = len(key)
        for i in range(1,k):
            subset = list(itertools.combinations(key,i))
            for j in subset:
                if freq_set[key]/freq_set[key-frozenset(j)]>=confidence:
                    Rule[key-frozenset(j)]=frozenset(j)
    return Rule


"""
Main Function
"""

if __name__ == '__main__':
    freq_set = apriori('GroceryStoreDataSet.csv',support=0.2)
    rule = rules(freq_set,confidence=0.5)
    for i in rule:
        print(i,'--->',rule[i])
