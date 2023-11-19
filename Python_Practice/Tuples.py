#Write a Python program to create a tuple with different data types.
def create_tuple(*args):
    print(tuple(args))
#create_tuple(1, 6, 8, 3, "A", "B")
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to add an item to a tuple.
def add_items(tup, val):
    print(tup + (val,))
#add_items((1,2,4,56,7,4), 69)

def add_items_using_lists(tup, val):
    lst = list(tup)
    lst.append(val)
    print(tuple(lst))
#add_items_using_lists((1,2,4,56,7,4), 69)

def add_items_at_index(tup, index, val):
    tup = tup[:index] + (val,) + tup[index:]
    print(tup)
#add_items_at_index((1,2,3,4,6,7,8,9,0), 4, 5)
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to convert a tuple to a string.
def tuple_to_string(tup):
    print(str(tup), type(str(tup)))
#tuple_to_string((1,2,3,4,5))

def tuple_to_string_2(tup):
    print("".join(tup))
#tuple_to_string_2(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to find repeated items in a tuple.
def repeated_items(tup):
    print([x for x in tup if tup.count(x) > 1])
#repeated_items(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))
#--------------------------------------------------------------------------------------------------------------------------------

#