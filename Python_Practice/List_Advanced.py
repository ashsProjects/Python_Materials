#Write a Python function to reverse a list at a specific location.
def reverse_at_loc(lst, start, end):
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    print(lst)
#reverse_at_loc([1,2,3,4,5,6,7,8,9], 2, 8)
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python function find the length of the longest increasing sub-sequence in a list.
def count_increasing(lst):
    count = 0
    max = 0
    for i in range(0, len(lst)):
        temp_lst = [x for x in range(i,len(lst) - 1) if lst[x + 1] > lst[x] + 1]
        count = len(temp_lst) + 1
        if count > max: max = count
    print(max)    
#count_increasing([10, 20, 30, 40, 50, 30, 30, 20])
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python function to find the kth smallest element in a list.
def kth_smallest(lst, k):
    lst.sort()
    print("{}th smallest value:".format(k),lst[k - 1])
#kth_smallest([6,2,8,12,4,7,0,6,3,6,8,0,45,65], 5)
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python function to find the kth largest element in a list. 
def kth_largest(lst, k):
    lst.sort()
    print("{}th largest value:".format(k), lst[-k])
#kth_largest([6,2,8,12,4,7,0,6,3,6,8,0,45,65], 6)
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python function to check if a list is a palindrome or not. Return true otherwise false.
def palindrome(lst):
    return lst == lst[::-1]
    
#print(palindrome(['Red', 'Green', 'Red']))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python function to remove duplicates from a list while preserving the order.
from collections import OrderedDict

def remove_duplicates(lst):
    print(list(OrderedDict.fromkeys(lst)))
#remove_duplicates([1,2,4,3,5,4,6,9,2,1])
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to find the first non-repeated element in a list.
def first_non_repeated(lst):
    for i in range(0, len(lst) - 1):
        l = [lst[x] for x in range(0, len(lst)) if lst[i] == lst[x]]
        print(l)
        if len(l) == 1: return lst[i]
    return "None"
#print(first_non_repeated([1, 2, 3, 4, 5, 6, 7, 8]))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to find all the pairs in a list whose sum is equal to a given value.
def sum_of_pairs(lst, _sum):
    return_lst = []
    dic = {}
    for n in lst:
        if _sum - n in dic:
            return_lst.append((n, _sum - n))
        else:
            dic[n] = _sum - n
    print(return_lst)
sum_of_pairs([1,2,3,4,5,6,7,8,9], 10)
