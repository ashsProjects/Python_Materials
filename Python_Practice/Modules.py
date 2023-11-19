import random
import datetime
import types
import decimal

#Write a Python program to select a random element from a list, set, dictionary-value, and file from a directory.
def randList(arr):
    print(random.choice(arr))
def randTuple(tup):
    print(random.choice(tup))
def randDict(dict):
    key = random.choice(list(dict))
    print(dict[key])
def randSet(s):
    print(random.choice(tuple(s)))

#randList([1,2,3,4,5,6])
#randTuple((10,20,30,40,50,60))
#randDict({"Name": "Ayush", "Age": 20, "Job":"Student"})
#randSet({100,200,300,400,500,600})
#--------------------------------------------------------------------------------------------------------------------------------
#Write a Python program to generate a random integer between 0 and 6 - excluding 6, random integer between 5 and 10 - excluding 10, 
# random integer between 0 and 10, with a step of 3 and random date between two dates.
def rand2():
    print("Random int 0-6: " + str(random.randrange(0,6)))
    print("Random int 5-10: " + str(random.randrange(5,10)))
    print("Random int 0-10 with step 3: " + str(random.randrange(0,10,3)))
    
    start_date = datetime.date(2023,1,1)
    end_date = datetime.date(2023,12,31)
    date_between_days= end_date - start_date
    days = date_between_days.days
    rand_day = random.randrange(days)
    rand_date = start_date + datetime.timedelta(days = rand_day)
    print("Random date: " + str(rand_date))   
#rand2()
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to shuffle the elements of a given list.
def randShuffle(arr):
    print("Before shuffle: " + str(arr))
    random.shuffle(arr)
    print("After shuffle: " + str(arr))   
#randShuffle(["A", 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "Joker"])
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to generate a float between 0 and 1, inclusive and generate a random float within a specific range.
def randFloat():
    print("Random Float: {:.3f}".format(random.uniform(0,1)))
#randFloat()
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to create a list of random integers and randomly select multiple items from the said list.
def addRandToList():
    arr = []
    for i in range(0,10): arr.append(random.randrange(0,100))
    print(random.sample(arr,5))
#addRandToList()
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to check if a function is a user-defined function or not. 
print(isinstance(addRandToList, types.FunctionType))#True if user-defined
print(isinstance(max, types.FunctionType))
#--------------------------------------------------------------------------------------------------------------------------------

# Write a Python program to construct a Decimal from a float and a Decimal from a string. Also represent the decimal value as a tuple.
def decimal1(flt, str):
    print("Decimal from a float: {}".format(decimal.Decimal(flt)))
    print("Decimal from a String: {}".format(decimal.Decimal(str)))
    print("Decimal Tuple: {}".format(decimal.Decimal(str).as_tuple()))
#decimal1(3.14159,"9.81")
#--------------------------------------------------------------------------------------------------------------------------------

