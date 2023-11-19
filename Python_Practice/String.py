#Write a Python program to count the number of characters (character frequency) in a string.
def count_chars(str):
    dict = {}
    for i in str:
        dict.update({i:str.count(i)})
    print(dict)
#count_chars("google.com")
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to get a string made of the first 2 and last 2 characters of a given string. 
# If the string length is less than 2, return the empty string instead.
def return_2s(str):
    if len(str) < 2: return ""
    else:
        return str[0:2] + str[-2::1]
#print(return_2s("pythonisfun"))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to get a string from a given string where all occurrences of its 
# first char have been changed to '$', except the first char itself.
def change_to_dollars(str):
    first_char = str[0]
    str = str[1:].replace(first_char, "$")
    print(first_char + str)
#change_to_dollars("restart")
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string. 
def swap_and_append(str1, str2):
    temp = str1[0:2]
    str1 = str2[0:2] + str1[-1]
    str2 = temp + str2[-1]
    return str1 + " " + str2  
#print(swap_and_append("abc", "xyz"))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python function that takes a list of words and return the longest word and the length of the longest one. 
def longest_word(arr):
    length = []
    for s in arr:
        length.append((len(s), s))
    length.sort()
    print("Longest word: {}\nLength of the longest word: {}".format(length[-1][1], length[-1][0]))
#longest_word(["Pseudostratified", "ciliated", "columnar", "epithelium"])
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to remove the nth index character from a nonempty string
def remove_index(string, index):
    return string.replace(string[index], "")
#print(remove_index("This is my Name", 1))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
def swap_first_and_last(str):
    return str[-1] + str[1:-1] + str[0]
#print(swap_first_and_last("Swapping"))    
#--------------------------------------------------------------------------------------------------------------------------------

# Write a Python script that takes input from the user and displays that input back in upper and lower cases.
def lower_upper(string):
    return ("In upper case: {}\nIn lower case: {}".format(string.upper(), string.lower()))
#print(lower_upper("XyphoId proCesS"))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
def four_copies(string):
    if len(string) < 2: return "The length must be at least 2"
    else:
        return string[-2:] * 4
#print(four_copies("mandible"))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python function to reverse a string if its length is a multiple of 4
def return_if_multiple(string):
    if len(string) % 4 == 0:
        return string[::-1]
    else: return "The string length is not a multiple of 4"
#print(return_if_multiple("declaratives"))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to display formatted text (width=50) as output.
import textwrap as tw
def formatted_text(string):
    print(tw.fill(string, width=500))
#formatted_text("Terminal B")
#--------------------------------------------------------------------------------------------------------------------------------

# Write a Python program to remove existing indentation from all of the lines in a given text.
def remove_indent(string):
    return string.replace("\n", " ")
#print(("My\nname\nis\nAsh\n"))
#print(remove_indent("My\nname\nis\nAsh\n"))
#--------------------------------------------------------------------------------------------------------------------------------

#V
def decimal_with_sign(a, b):
    print("Original Number: {0}\nFormatted Number: {0:+.2f}\nOriginal Number: {1}\nFormatted Number: {1:+.2f}"\
        .format(a, b))
#decimal_with_sign(2.12321,-3.141591121313)
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to display a number with a comma separator.
def comma(num):
    return "Number with commas: {:,}".format((num))
#print(comma(1000002))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to format a number with a percentage. 
def percent(num):
    return "Number formatted as %: {:.2%}".format(num)
#print(percent(.69))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to display a number in left, right, and center aligned with a width of 10.
def alignment(num):
    print("Left aligned: "+"{:< 10d}".format(num))
    print("Right aligned: "+"{:10d}".format(num))
    print("Center aligned:"+"{:^10d}".format(num))
#alignment(15)
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to count occurrences of a substring in a string.
def count_substrings(string, substr):
    print(string.count(substr))
#count_substrings("Programs in Python", "Py")
#--------------------------------------------------------------------------------------------------------------------------------

# Write a Python program to reverse words in a string.
def reverse_words(arr):
    reversed_string = map(lambda x: x[::-1], arr)
    print("Before Reverse: ", arr)
    print("After reverse: ", list(reversed_string))
#reverse_words(["Hello", "My", "Name", "Is", "Ash"])
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to check whether a string contains all letters of the alphabet.
import string
def check_alphabets(s):
    alphabets = set(string.ascii_lowercase)
    return len(set(s.lower())) >= len(alphabets)#account for the space character in the string
#print(check_alphabets("The quick brown fox jumps over the lazy dog"))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to lowercase the first n characters in a string.
def lowercase_first_n(s, num):
    new_arr = [i.upper() for i in list(s)[:num] if 1 == 1]
    print(new_arr + list(s)[num::])
#lowercase_first_n("arrays and lists", 2)
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to count and display vowels in text
#print(len([s for s in "Print all the vowels in the sentence" if s in "aeiouAEIOU"]))
#print([s for s in "Print all the vowels in the sentence" if s in "aeiouAEIOU"])
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to count characters at the same position in a given string (lower and uppercase characters) as in the English alphabet.
def letters_in_same_position(s):
    count = 0
    lower_case = list(string.ascii_lowercase)
    upper_case = list(string.ascii_uppercase)
    for i in range(0, len(s)):
        if list(s)[i] == lower_case[i] or list(s)[i] == upper_case[i]: count += 1
    return count
#print(letters_in_same_position("Aacdjhkhkio"))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to find the smallest and largest words in a given string.
def smallest_largest(s):
    s_list = s.split(" ")
    s_dict = {}
    for i in s_list:
        s_dict.update({i:len(i)})
    print("Largest word: {}".format(max(s_dict, key=s_dict.get)))
    print("Smallest word: {}".format(min(s_dict, key=s_dict.get)))
#smallest_largest("Write a Java program to sort an array of given integers using Quick sort Algorithm.")
#--------------------------------------------------------------------------------------------------------------------------------
def return_nums(s):
    strs = s.split(" ")      
    digits = [int(i) for i in strs if i.isdigit()]
    print(digits)
#return_nums("Red 12 Black 45 Green")
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to split a multi-line string into a list of lines.
def multi_line(s):
    print(s.split("\n"))
#multi_line("This\nis a\nmultiline\nstring.\n")    
#--------------------------------------------------------------------------------------------------------------------------------

# Write a Python program to extract and display the name from a given Email address.
def extract_name(email):
   index_of = email.index("@")
   print(email[:index_of:])
#extract_name("example.bish@gmail.com")
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program that takes two strings. Count the number of times each string contains the same three letters at the same index
def count_same_index(str1, str2):
    count = 0
    i = 0
    for s in range(0,len(str1) - 2):
        if str1[i:i+3] == str2[i:i+3]:
            count += 1
            i += 1
    print(count)
count_same_index("Red Green", "Red Green")