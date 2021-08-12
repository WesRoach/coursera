# 3
# array = [1,3,5,2,4,6]

# 4
# array = [1,5,3,2,4]

# 10
# array = [5,4,3,2,1]

#5
# array = [1,6,3,2,4,5]

# 56
# array = [9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0]

# 590
# array = [37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45]

# 2372
array = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]


# open file and create array
fname = '/Users/admin/Dropbox/Learn2Code/Coursera/StanfordAlgorithms/week2/assignment/assignmentArray.txt'

with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [int(x.strip()) for x in content]

# inversions = 2407905288

# print(content)

# iterate through array comparing each value to each other value only once
# Brute Force
def bruteInv(array):
    cnt = 0
    for i in range(len(array) - 1):
        print("i: {}".format(i))
        for j in array[i + 1:]:
            # print("i: {}, j: {}".format(array[i], j))
            if array[i] > j:
                cnt += 1
        print("cnt: {}".format(cnt))
    print("inversions: {}".format(cnt))

# bruteInv(array)

count = 0

def merge_sort(li):
    # base case
    if len(li) < 2: return li
    # split list in half
    m = len(li) / 2
    # pass left/right halves to merge()
    return merge(merge_sort(li[:m]), merge_sort(li[m:]))

def merge(l, r):
    global count
    result = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            count = count + (len(l) - i)
            j += 1
    # if reached end of one list - add remaining of second list to end of result
    result.extend(l[i:])
    result.extend(r[j:])
    return result

print merge_sort(content)
print count


# def merge_sort(li):

#     if len(li) < 2: return li
#     m = len(li) / 2
#     return merge(merge_sort(li[:m]), merge_sort(li[m:]))


# def merge(l, r):
#     global count
#     result = []
#     i = j = 0
#     while i < len(l) and j < len(r):
#         if l[i] < r[j]:
#             result.append(l[i])
#             i += 1
#         else:
#             result.append(r[j])
#             count = count + (len(l) - i)
#             j += 1
#     result.extend(l[i:])
#     result.extend(r[j:])
#     return result

# print merge_sort(array)
# print count
