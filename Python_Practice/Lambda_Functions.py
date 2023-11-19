#Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
# also create a lambda function that multiplies argument x with argument y and prints the result.
l = lambda x: x + 15
#print(l(10))
p = lambda x, y: x * y
#print(p(2,5))
#--------------------------------------------------------------------------------------------------------------------------------

# Write a Python program to sort a list of tuples using Lambda.
lst = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
lst = sorted(lst, key=lambda x: x[1])
#print(lst)
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to filter a list of integers using Lambda.
lst2 = [1,2,3,4,5,6,7,8,9]
evens = list(filter(lambda x: x % 2 == 0, lst2))
odds = list(filter(lambda x: x % 2 == 1, lst2))
#print(evens)
#print(odds)
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to square and cube every number in a given list of integers using Lambda.
#print("Squared: ", list(map(lambda x: x**2, lst2)))
#print("Cubed: ", list(map(lambda x: x**3, lst2)))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to find if a given string starts with a given character using Lambda. 
str1 = "Anthony"
r = lambda x: str1.startswith(x)
#print(r("a"))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to find the intersection of two given arrays using Lambda
list1 = [1,2,3,5,7,8,9,10]
list2 = [1,2,4,8,9]
li = list(filter(lambda x: x in list1, list2))
#print(li)
#--------------------------------------------------------------------------------------------------------------------------------

#