# Loops in general:
# traverse -> to actually visit that entity and operate on it.

'''
In CS, loops are set of statements that are executed sequentially over a given list, string, tuple, dictionary, set, array etc.
iterate -> to go through something in a pre-defined fashion.
to perform iteration, we use an iterator. 
An iterator travels or traverse from a starting point to an ending point.
an iterator is always a variable.


list = [1,2,3,4,5,6,7]
        0 1 2 3 4 5 6
        i -> iterator
        starting index = 0
        end index = 6
        predefined fashion = linear traversal

tuple = ()

dict = {}

string = ""
'''

# Types of loops: -> for, while, do-while

# For loops:

list = [1,2,3,4,5,6,7,8]
# print(f'len: {len(list)}')

# for i in range(0, len(list)):
#   print (list[i])


# for i in range(0, len(list), 2):
#   print (list[i])


# range(starting_index, ending_index + 1)

# for i in range(1, len(list), 2):
#     print(list[i])



'''
 range() => range(a, b, c): takes three parameters
  a -> starting Index
  * b -> [must]
  c -> jump of the iterator

  a = 0;
  b = must
  c = 1 (default)
'''

# for in a list:

# list = [1,2,3,4,5]
# for i in range(0, ):
#   print (list[i])



# t = (10,30,40,50,60)
# si = 0
# ei = len(t) - 1

# for i in range(si, ei + 1):
#   print(t[i])


# string = "Akanksha"  # Aakh
# # for i in range(0, len(string)):
# #   print(string[i])

# for i in range(0, len(string), 2):
#         print(string[i])

dict = {
    'city': ["Gaon", "Rajwaada", "basti"],
    'name': ["Sanatan", "Akanksha", "Laaloo"],
    'car': ["Bailgaadi", "bhains", "Bakri"]
}

# print(dict.values())
# for i in dict.values():
#     for j in i:
#         print(j)
# for - each loop:
# generic - for loop

# nums = [1, 2, 3, 4, 5]


# Range based simple for loop:

# for index in range(0, len(nums)):
#   print(list[index])


# for - each element based for each loop
# for element in nums:
#   print(element)



'''
WAP to iterate through the given list and store each element in a seperate list, print the list.
'''
# copy = [10,50,100]
# copy = []
# list = [10,30,50,70,100]
# for i in range(0, len(list), 2):
#   copy.append(list[i])

# print(copy)


# String str = "Akanksha", print a string by copying the first four alphabets of the given string + "tail":

# str_k = "Akanksha"
# str_final = ""

# for i in range(0, 4):
#   str_final = str_final + str_k[i]

# print(str_final)
# str_final += "tail"
# print(str_final)


# list = ['a','b','c','d','e','f','g']
# # print the string "abcdefg"

# str_p = ""

# for i in range(0, len(list)):
#   str_p = str_p + list[i]
  
# print(str_p)


# num = [1,2,3,4,5]
# # Print the sum of the digits:

# sum = 0

# for i in range(1, len(num), 2):
#   sum = sum + num[i]
  
# print(sum)


## while loop:

# for i in range(0, 4):
#   print (i)



# entry controlled loop:

# i = 0
# while i < 4:
#   print(i)
#   i = i + 1

# print("loop has ended")

# string = "miakhalifa"
# string_cpy = ""

# i = 0
# while i < len(string):
#   string_cpy = string_cpy + string[i] 
#   i = i + 1


# print(string_cpy)


# list = [1,3,5,7,9]
# # print the sum using while loop:

# sum = 0

# i = 0 
# while i < len(list):
#   sum = sum + list[i]
#   i = i + 1
  
# print(sum)

# print the sum of first ten natural numbers:

# product = 1

# i = 1
# while i < 6:
#   product = product * i
#   i = i + 1

# print(product)


# product = 1

# for i in range(1, 6):
#   product = product * i
  
# print(product)



# do - while loop -> exit controlled loop:
# break = with an if statement to get out of a loop or an execution block
# i = 0

# while True:
#   print (i)
#   i = i + 1
#   if(i > 5):
#     break


# list = [1,2,3,4,5,6]

# for i in range(0, len(list)):
#   print(list[i])
#   if list[i] == 3:
#     break



# Continue statement -> skip over an element:

# list = [1,2,3,4,5,6]

# for i in range(0, len(list)):
#   if (i == 4):
#     continue
#   print (list[i])



  