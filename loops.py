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
