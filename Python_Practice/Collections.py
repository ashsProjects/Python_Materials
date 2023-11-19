from collections import Counter #counter counts iterable objects
from collections import deque #used for linked lists, fast appends and removes on both ends
import re
from collections import defaultdict

#Write a Python program that iterates over elements as many times as its count.
def print_counters(**kwargs):
    c = Counter(**kwargs)
    print(list(c.elements()))
#print_counters(a=1, b=4, c=6)
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to find the most common elements and their counts in a specified text.
def most_common_elements(txt):
    c = Counter(txt)
    print(c.most_common(3))
#most_common_elements("lkseropewdssafsdfafkpwe")
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to create a new deque with three items and iterate over the deque's elements. 
def create_deque(*args):
    d = deque(args)
    print(d)
    for element in d:
        print(element)
#create_deque(4,6,8,9,0,2)
#--------------------------------------------------------------------------------------------------------------------------------

# Write a Python program to find the occurrences of the 10 most common words in a given text. 
def ten_most_common(txt):
    words = re.findall("\w+", txt)
    c = Counter(words)
    print(c.most_common(10))
txt = """The Python Software Foundation (PSF) is a 501(c)(3) non-profit 
corporation that holds the intellectual property rights behind
the Python programming language. We manage the open source licensing 
for Python version 2.1 and later and own and protect the trademarks 
associated with Python. We also run the North American PyCon conference 
annually, support other Python conferences around the world, and 
fund Python related development with our grants program and by funding 
special projects."""
#ten_most_common(txt)
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program that accepts some words and counts the number of distinct words. Print the number of 
# distinct words and the number of occurrences of each distinct word according to their appearance.
def count_distinct_words(txt):
    txt = txt.split(" ")
    c = Counter(txt)
    print(c.items())
#count_distinct_words("red green red red green blue white black black")
#--------------------------------------------------------------------------------------------------------------------------------

# Write a Python program to create a deque and append a few elements to the left and right. 
# Next, remove some elements from the left and right sides and reverse the deque
def add_remove_deque(*args, addition, removal):
    dq = deque(args)
    print("Original Deque: ", dq,"\n")
    print("Adding items to the right (tail): ")
    dq.append(addition)
    print(dq,"\n")
    print("Adding items to the left (head): ")
    dq.appendleft(addition)
    print(dq, "\n")
    print("Removing items from the right (tail): ")
    dq.pop()
    print(dq, "\n")
    print("Removing items from the left (head): ")
    dq.popleft()
    print(dq, "\n")
    print("Removing removal var from the deque: ")
    dq.remove(removal)
    print(dq, "\n")
    print("Reversing the deque: ")
    dq.reverse()
    print(dq)
#add_remove_deque(1,2,3,4,5,6,7, addition=40, removal=5)
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to create a deque from an existing iterable object.
def create_from_existing(tup):
    dq = deque(tup)
    print(dq, type(dq))
#create_from_existing((4,7,2,4,8))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to count the number of times a specific element appears in a deque object.
def count_deque(*args):
    dq = deque(args)
    c = Counter(dq)
    print(c)
    i = input("Enter the number you want to check: ")
    print(dq.count(int(i)))
#count_deque(2,9,0,8,2,4,0,9,2,4,8,2,0,4,2,3,4,0)
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to calculate the maximum aggregate from the list of tuples (pairs)
def max_agg_list(lst):
    temp = defaultdict(int)
    for i, j in lst:
        temp[i] += j
    print(max(temp.items(), key=lambda x: x[1]))
max_agg_list([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])