import numpy as np
import math
import random
import os
import functools as ft

#Write a Python program that calculates the area of a circle based on the radius 
def areaOfCircle(radius):
    return np.pi * radius**2
#print(areaOfCircle(1.1))
#--------------------------------------------------------------------------------------------------------------------------------

# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
#fName = input("Enter your First Name: ")
#lName = input("Enter your Last Name: ")
#print("Your name is " + fName + " " + lName)
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program that accepts a sequence of comma-separated numbers 
#from the user and generates a list and a tuple of those numbers.
def list_tuple(*args):
    print(tuple(args))
    print(list(args))
#list_tuple(1,2,3,4,5,6,7,2,4,2)
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to display the first and last colors from the following list.
def first_last(arr):
    print(arr[0])
    print(arr[len(arr) - 1])
#first_last(["Yellow", "Green", "Red"])
#--------------------------------------------------------------------------------------------------------------------------------

# Write a Python program that accepts a filename from the user and prints the extension of the file
def print_extension(str):
    filename = input("Enter the file name: ")
    file_ext = filename.split(".")
#print(print_extension(file_ext[-1]))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
def nnn():
    val = int(input("Enter an integer value: "))
    comp_val = val + val**2 + val**3
    return comp_val
#print(nnn())
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to get the volume of a sphere with radius six.
def volume_of_sphere(x):
    vlm = (4/3) * math.pi * (x**3)
    return vlm
#print(volume_of_sphere(6))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to calculate the difference between a given number and 17. 
# If the number is greater than 17, return twice the absolute difference. 
def difference_17(x):
    diff = int(x) - 17
    if diff > 17: return diff * 2
    else: return diff
#print(difference_17(35))
#--------------------------------------------------------------------------------------------------------------------------------

# Write a Python program to test whether a number is within 100 of 1000 or 2000
def rangeOf100(x):
    if abs(x - 1000) <= 100 or abs(x - 2000) <= 100:
        return "Yes"
    else: return "No"
#print("Is the number within the range? " + rangeOf100(1999))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
def sumOfThreeNums(a, b, c):
    if a == b == c:
        return a ** 3
    else: return a + b + c
#print(sumOfThreeNums(5,5,5))
#--------------------------------------------------------------------------------------------------------------------------------

# Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. 
# Return the string unchanged if the given string already begins with "Is".

def attachToString(str):
    if str[0:2] == "Is": return str
    else: return "Is" + str
#print(attachToString("ash"))
#--------------------------------------------------------------------------------------------------------------------------------

# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
def returnNumOfString(str, num):
    for i in range(0,num):
        print(str)
#returnNumOfString("Ravioli", 10)
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to count the number 4 in a given list.
def printNumOf(arr, num):
    count = arr.count(num)
    return count
#print(printNumOf([1,2,1,2,111,11,1,1,1,1,14,5,3], 111))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. 
# Return n copies of the whole string if the length is less than 2.
def returnCopies(str, num):
    if len(str) > 2:
        for i in range(0, num): print(str[0:2])
    else: 
        for i in range (0, num): print(str)
#returnCopies("Momma", 3)
#--------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------
def checkVowel(char):
    if char in ['a', 'e', 'i', 'o', 'u']: return "Is a vowel"
    else: return "Is not a vowel"
#print(checkVowel('y'))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program that checks whether a specified value is contained within a group of values.
def checkContains(val, *args):
    if val in args: return "True"
    else: return "False"
#print(checkContains(10, 1,2,3,4,6,2,4,3,2))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to create a histogram from a given list of integers.
def hist(*args):
    arr = []
    freqArr = []
    for i in args:
        if i not in arr:
            freqArr.append(args.count(i))
            arr.append(i)
    for j in freqArr:
        for num in range(0,j):
            print("*", end="")
        print("")
#hist(1,1,1,1,1,1,1,2,3,4,5,5,5,5,3,3,4,6)
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to print all even numbers from a given list of numbers in 
# the same order and stop printing any after 237 in the sequence.
def print_even_in_list(arr):
    for n in arr:
        if n != 237:
            if n % 2 == 0: print(n, end= " ")
        else: break
#print_even_in_list([386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 237, 1])
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
def gcd(x, y):
    gcd = 1   
    if x % y == 0:return y   
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break 
    return gcd
#print(gcd(336,330))
#--------------------------------------------------------------------------------------------------------------------------------

def solveIfTwoInt(a, b):
    if type(a) == type(b):
        return a + b
    else: return "Both not integers"
#print(solveIfTwoInt(1,10))
#--------------------------------------------------------------------------------------------------------------------------------

# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
def differentNumbers(arr):
    if len(arr) == len(set(arr)): return "True"
    else: return "False"
#print(differentNumbers([1,2,3,4,5,6,1,2]))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program that removes and prints every third number from a list of numbers until the list is empty.
def removeThird(arr):
    while arr:
        for i in arr[2::3]:
            print(i)
            arr.remove(i)
#removeThird([1,2,3,4,5,6,7,8,9])
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to identify unique triplets whose three elements sum to zero from an array of n integers
def triplets(arr):
    triplets = []
    positiveArrSet = list(set(filter(lambda x: x >= 0, arr)))
    negativeArrSet = set(filter(lambda x: x < 0, arr))
    
    for i in negativeArrSet:
        index = 0
        for j in positiveArrSet[:-1]: 
            if i + j + positiveArrSet[index + 1] == 0: triplets.append(tuple((i, j, positiveArrSet[index + 1])))
            index += 1
    
    return triplets

#print(triplets([1, -1, 0, 4, 8, -4, 2, 5, 3, -7, 4]))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five.
def occurences(arr):
    count_of_nineteen = 0
    count_of_five = 0
    for i in arr:
        if i == 19: count_of_nineteen += 1
        if i == 5: count_of_five += 1
    if count_of_five >= 3 and count_of_nineteen == 2: return "True"
    else: return "False"
#print(occurences([19,19,5,3,5,5,5]))
#print(occurences([19,15,15,3,5,5,2]))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program that accepts a list of integers and calculates the length and the fifth element. 
# Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
def lengthAndFifth(arr):
    fifth = arr[4]
    count = 0
    for i in arr:
        if i == fifth: count += 1
    if count == 3 and len(arr) == 8: return "True"
    else: return "False"
#print(lengthAndFifth([19,19,15,5,5,5,1,2]))
#print(lengthAndFifth([19,15,5,5,1,2]))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to check the nth-1 string is a proper substring of the nth string in a given list of strings.
def checkLastTwo(arr):
    return (arr[-2]) in (arr[-1])
#print(checkLastTwo(['a', 'abb', 'sfs', 'oo', 'de', 'sfde']))
#--------------------------------------------------------------------------------------------------------------------------------

#
