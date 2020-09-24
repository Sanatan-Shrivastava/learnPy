"""
list are containers in which we store, manipulate, or read data from.
These are ordered, and changaeble.
These allow duplicates members/elements.



###### Indexing is always 0-based unless mentioned in the question:
represented by sqaure brackets name_of_list = []
"""

# They are used to store more than one values:

nums = [1,2,3,4,5,6,7,8,9]
family = ["Ajay", "Chetna", "Akanksha", "Ashi", "Pappi Bua"]
   
# # print the list:
# print(family)
# print(nums)

# # print the element at a given index:
# print(family[0])
# print(nums[0])


# # print the element in list "family", present on location index  k = 4. (Indexing is 1-based)
# # Formula -> k - starting index
# newIndex  = 3
# print(family[newIndex])

# # Finding the length of the list: 
# lenA = len(nums)
# lenB = len(family)
# fam_list = [lenA, lenB]
# print(fam_list)



# # Append (add to the last of the list): list.append(argument)

# family.append("Akku")
# print(family)

# # Remove from the list: (remove the element at the given index:)

# family.remove(family[4])
# print(family)

# # Insert at the index:  list.insert(index, "string")

# family.insert(3, "Sanatan")
# print(family)

# let us change the value at a given index:

# family[4] = "Sanatan"
# print(family)

# Remove the last element from the list: pop();
# print(family)
# a = family.pop()
# print(a)
# print(family)


# Reverse():
# family.reverse()
# print(family)


# sort() a list:

# marks = [350, 540, 120, 500]
# # marks.sort()
# # marks.reverse()
# # print(marks)


# # Reverse Sort:

# marks.sort(reverse = False)
# print(marks)
chars = ['a','c','b','d']
chars.sort()
print(chars)