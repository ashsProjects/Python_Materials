#Write a Python program to iterate over sets.
def iterate_sets(s):
    for x in s:
        print(x)
#iterate_sets({1,2,3,4,5})
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to add member(s) to a set.
def add_to_set(s, val):
    print("Before add: ", s)
    s.add(val)
    print("After add: ",s)
#add_to_set({1,2,3,4,5}, 20)

def add_multiple(s, val_list):
    s.update(val_list)
    print(s)
#add_multiple({1,2,3,4,5,6}, [20,30,40,50])
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to remove item(s) from a given set.
def remove_items(s, val):
    #s.discard(val)#does not raise an error wif val does not exist
    s.remove(val)#raises an error if val does not exist
    #s.pop()#removes a random item from the set
    print(s)
#remove_items({1,2,3,45,6,7}, 6)

def remove_multiple_items(s, val):
    s.difference_update(val)
    print(s)
#remove_multiple_items({1,2,3,45,6,7}, [1,2,3])
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to create an intersection of sets.
def intersection(set1, set2):
    print(set1.intersection(set2))#intersection is the values in both sets
#intersection({1, 2, 3, 4, 5, 6}, {1,2,0,55,66,77,88})

#Write a Python program to create a union of sets
def union(set1, set2):
    print(set1.union(set2))#union is values in  both sets
#union({1, 2, 3, 4, 5, 6}, {1,2,0,55,66,77,88})

#Write a Python program to create set difference. 
def difference(set1, set2):
    print(set1.difference(set2))#differece is the values in one but not in the other
#difference({1, 2, 3, 4, 5, 6}, {1,2,0,55,66,77,88})

#Write a Python program to create a symmetric difference.
def symmetric_difference(set1, set2):
    print(set1.symmetric_difference(set2))#Values in both sets but not ones that both sets have
#symmetric_difference({1, 2, 3, 4, 5, 6}, {1,2,0,55,66,77,88})
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to check if a set is a subset of another set.
    #Cam also use the issubset() method to check for subsets
def subset(set1, set2):
    if set1.intersection(set2) == set2: print("True")
    else: print("False")
#subset({1,2,3,4,5,6},{1,2})
#subset({'mango', 'apple'},{'mango'})
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings.
def unique_words(lst):
    set1 = set(lst)
    count = {}
    for words in set1:
        count[words] = lst.count(words)
    print(count)
unique_words(["a", "boy", "and", "a", "girl", "went", "to", "school", "together", "in", "the", "morning"])

