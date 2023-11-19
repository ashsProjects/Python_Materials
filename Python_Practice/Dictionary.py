import operator

# {"Name":"Ash", "Age": 21, "School":"CSU", "Major":"Computer Science", "GPA":3.960}
# {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# Write a Python script to sort (ascending and descending) a dictionary by value.
def sort_dict(dic):
    dic = sorted(dic.items(), key=operator.itemgetter(0))
    print(dic)
#sort_dict({"Name":"Ash", "Age": 21, "School":"CSU", "Major":"Computer Science", "GPA":3.960})
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python script to add a key to a dictionary.
def add_key(dic, key_value):
    dic.update(key_value)
    print(dic.items())
#add_key({"Name":"Ash", "Age": 21, "School":"CSU", "Major":"Computer Science", "GPA":3.960}, {"Height":"5'10"})
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python script to concatenate the following dictionaries to create a new one
def concat_dic(dic1, dic2, dic3):
    dic1.update(dic2)
    dic1.update(dic3)
    print(dic1.items())
#concat_dic({1:10, 2:20}, {3:30, 4:40}, {5:50,6:60})
#--------------------------------------------------------------------------------------------------------------------------------

# Write a Python script to check whether a given key already exists in a dictionary
def check_key(dic, key):
    return key in dic.keys()
#print(check_key({"Name":"Ash", "Age": 21, "School":"CSU", "Major":"Computer Science", "GPA":3.960}, "Name"))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to iterate over dictionaries using for loops.
def iterate_dic(dic):
    for i in dic.items():
        print(i)
#iterate_dic({"Name":"Ash", "Age": 21, "School":"CSU", "Major":"Computer Science", "GPA":3.960})
#--------------------------------------------------------------------------------------------------------------------------------

# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
def num_between_1n(n):
    dic = dict()
    for i in range(1, n + 1):
        dic[i] = n * n
    print(dic.items())
#num_between_1n(10)
#--------------------------------------------------------------------------------------------------------------------------------

# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
def num_between_1and15():
    dic = dict()
    for i in range(1,16):
        dic[i] = i * i
    print(dic.items())
#num_between_1and15()
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to sum all the items in a dictionary.
import functools as ft
def sum_dict(dic):
    print(ft.reduce(lambda x, y: x + y, dic.values()))
#sum_dict({'data1':100,'data2':-54,'data3':247})
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to multiply all the items in a dictionary.
def product_dict(dic):
    print(ft.reduce(lambda x, y: x * y, dic.values()))
#product_dict({'data1':10,'data2':5,'data3':3})
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to remove a key from a dictionary. 
def remove_key(dic, key):
    print("Removed", dic.pop(key))
    print(dic.items())
#remove_key({"Name":"Ash", "Age": 21, "School":"CSU", "Major":"Computer Science", "GPA":3.960}, "GPA")
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to map two lists into a dictionary.
def map_lists(lst1, lst2):
    dic = dict(zip(lst1, lst2))
    print(dic.items())
#map_lists([1,2,3,4,5], [0,9,8,7,6])
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to sort a given dictionary by key.
def sort_by_key(dic):
    for key in sorted(dic):
        #print("%s: %s" % (key, dic[key]))
        print("{}: {}".format(key, dic[key]))
#sort_by_key({'red':'#FF0000', 'green':'#008000', 'black':'#000000', 'white':'#FFFFFF'})
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to get the maximum and minimum values of a dictionary
def max_and_min(dic):
    print("Maximum Vale: ", max(dic.values()))
    print("Minimum Vale: ", min(dic.values()))
    
#max_and_min({'x':500, 'y':5874, 'z': 560, 'a': 2, 'b': 79})
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to remove duplicates from the dictionary. 
def remove_duplicates(dic):
    nd_dic = {}
    for key, value in dic.items():
        if key not in nd_dic:
            nd_dic[key] = value
    print(nd_dic)
#remove_duplicates({'x':500, 'y':5874, 'z': 560, 'a': 2, 'b': 79, 'x':500})
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to check if a dictionary is empty or not.
def check_empty(lst):
    print("Not empty") if len(lst) > 0 else print("Empty")
#check_empty({})
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to combine two dictionary by adding values for common keys.
from collections import Counter
def combine_two_dicts(dic1, dic2):
    print(Counter(dic1) + Counter(dic2))
#combine_two_dicts({'a': 100, 'b': 200, 'c':300},{'a': 300, 'b': 200, 'd':400})
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to find the key of the maximum value in a dictionary.
def find_max_key(dic):
    print("Maximum: " + max(dic, key=dic.get), "\nMinimum: " + min(dic, key=dic.get))
#find_max_key({'a': 300, 'b': 200, 'd':400})