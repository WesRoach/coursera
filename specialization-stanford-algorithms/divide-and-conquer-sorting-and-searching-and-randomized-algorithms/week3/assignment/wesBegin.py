#!/usr/bin/python

# 10: 25 31 21

# 100: 620 573 502

# 1000: 11175 10957 9735

# 100000: 162085 164123 138382

import math, sys

# open file and create array
fname = '/Users/admin/Dropbox/Learn2Code/Coursera/StanfordAlgorithms/week3/assignment/quicksortArray.txt'

with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [int(x.strip()) for x in content]

# Reduce input file to first n elements
limit = content[:int(sys.argv[1])]

print(limit)

cnt = 0

def partition(array, begin, end, pivot):
    i = begin + 1
    global cnt
    cnt += end - begin
    array[begin], array[pivot] = array[pivot], array[begin]
    pivot = begin
    for j in range(begin + 1, end + 1):
        if array[j] < array[pivot]:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[begin], array[i - 1] = array[i - 1], array[begin]
    return i - 1

def choosePivot(array, begin, end):
    return begin

def quicksort(array, begin, end):
    if len(array[begin:end+1]) < 2: return
    p = choosePivot(array, begin, end)
    retP = partition(array, begin, end, p)
    quicksort(array, begin, retP - 1) # left
    quicksort(array, retP + 1, end) # right
    return

quicksort(limit, 0, len(limit)-1)
print(limit)
print(cnt)
