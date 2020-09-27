"""
Tuples: Sequences/Container to store the data.
-> This is only read-type data container.
-> You cannot modify, manipulate, write into a tuple (immutable)
-> unchangaeble, and they are ordered.
-> Used where list is causing ambiguity.
* indexed by integers.
* read only list:
0 tuple -> empty tuple.

represented by (); (optional)
"""
# To create an empty tuple:
tup = ()

# to print the tuple
# print(tup)

# to print the data type of tuple (type()):
# print(type(tup))


# an integer
# tup_int = 10
# print(type(tup_int))


# a tuple

# tup_tuple = 10,
# print(type(tup_tuple))

# Tuple is also integer-index based:

a = 10,20,30,40,50,60,50

# access an element at index i; tuple[i] -> element
'''
a[0] = 10
a[1] = 20
a[2] = 30
a[3] = 40
'''

# slicing
# print(a[1:])
# print(a[0:4])
# print(a[-3:-1])

# Deleting a tuple:
del (a)


# Basic Tuple Operations : concatenation, repitition, membership

a = 10,30,60,90,100
b = 40,50,60,80,90

# Concatenate two tuples:
# print(a + b)

# Reptition of tuples:
a = 3*a
print(a)


# Membership: (if a given number is an element of a tuple)
# print(10 in a)
# print(50 in a)


# to find the length of the tuple:
# print(len(a))



# Special functions of tuple:
# * Compare two tuples: 
'''
to compare two tuples: cmp(tuple_1, tuple_2)
returns -1, if tuple_1 < tuple_2
returns 0 if tuple_1 == tuple_2
returns 1 if tuple_1 > tuple_2
'''

print(cmp(a, b))

# to find the maximum element in tuple: max(tuple_name)

print(max(a))

# to find the minimum element in tuple: max(tuple_name)

print(min(a))

str = "sanatan-shrivastava-is-an-asshole"
print(tuple(str)) #stores character of a string in tuple
print(tuple(str.split("-"))) #stores words of string sepreated by a '-' in tuple
print(tuple(str.split())) # stores the entire string in a tuple




"""

1	The literal syntax of list is shown by the [].	The literal syntax of the tuple is shown by the ().
2	The List is mutable.	The tuple is immutable.
3	The List has the a variable length.	The tuple has the fixed length.
4	The list provides more functionality than a tuple.	The tuple provides less functionality than the list.
5	The list is used in the scenario in which we need to store the simple collections with no constraints where the value of the items can be changed.	The tuple is used in the cases where we need to store the read-only collections i.e., the value of the items cannot be changed.
6	The lists are less memory efficient than a tuple.	The tuples are more memory efficient because of its immutability.

"""


# Tuple can store tuple in tuple
out = ()
in_1 = (1,2,3)
in_2 = (4,5,6)
in_3 = in_1 + in_2
out = (in_1, in_2)
print(out)
print(in_3)

# List can store list

class9 = []
tu = (1,2,3,4)
class10 = [tu, tu, tu, tu]
phy = [1,2,5,6]
chem = [4,9,7,8]
maths = [0,11,32,54]
commerce = [50,403,430]

class9 = [phy, chem, maths, commerce]
print(class10)

