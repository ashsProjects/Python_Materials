#sort a list of nummbers
#Precondition: lst is a list of numbers in arbritary order
#Postcondition: the list is a permuatation of the input lst
#   and is sorted in ascending order
#Loop Invariant: For the outer loop, i is an integer such that i <= len(lst)
#   and for the inner loop, j <= len(list) - i - 1
def bubble_sort(lst):
  list_len = len(lst)
  
  #i < list_len
  for i in range(list_len - 1):
    #i < list_len
    
    #i < list_len - i - 1
    for j in range(0, list_len - i - 1):
      #i < list_len - i - 1
      if lst[j] > lst[j + 1]:
        temp = lst[j]
        lst[j] = lst[j + 1]
        lst[j + 1] = temp
      #i < n
    #i >= list_len - i - 1
    
    # i < list_len
  #i >= list_len
  return lst


#sort a list of nummbers
#Precondition: lst is a list of numbers in arbritary order
#Postcondition: the list is a permuatation of the input lst
#   and is sorted in ascending order
#Loop Invariant: For the outer loop, i is an integer such that i <= len(lst) - 1
#   and for the inner loop, j >= i + 1 and j < list_len
def selection_sort(lst):
  list_len = len(lst)
  
  #i < list_len - 1
  for i in range(list_len - 1):
    #i < list_len - 1
    min = 1
    
    #j >= i + 1 and j < list_len
    for j in range(i + 1, list_len):
      #j >= i + 1 and j < list_len
      if lst[j] < lst[min]:
        min = j
      #j >= i + 1 and j < list_len
    #j > i + 1 and j >= list_len
    
    temp = lst[i]
    lst[i] = lst[min]
    lst[min] = temp
    #i < list_len - 1
  #i >= list_len - 1
  return lst

print(selection_sort([4,3,2,1]))