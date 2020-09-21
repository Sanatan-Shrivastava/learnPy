# """
# string = "sanatan"

# string = m a l a y s i a
#          0 1 2 3 4 5 6 7
# """
# string = "malaysia"
# # substring = part of a string -> continous -> malay is a substring of malaysia
# # subsequence = part of a string -> discontinous -> maay is a subsequence of malaysia
# # quick access: 

# print(string[0])
# print(string[3])
# print(string[-1])
# print(string[-2])

# # Index-range based printing/operations:
# # printing substrings:
# # print(string[startindex : endindex + 1])
# # print(string[startindex : ]) = print(string[startindex : lastindex])
# # print(string[ : endindex]) = print(string[0 : endindex])

# print(string[2:5])
# print(string[:5])
# print(string[:])
# print(string[3:])
# print(string)
# print(string[0:8])
# print(string[0:])
# print(string[:])
# print(string[100000:13120930129039])

# # malaysiamalaysia
# print(string*4)
# print(string*3)

# # two equals are equal or not:

# strA = "sanatan"
# strB = "sanatan"
# is_equal = (strA == strB)
# print(is_equal)
# print(type(is_equal))


# # print(string[startindex : endindex + 1])
string = "python"

# error: assignment is not available, strings are immutable in python: -> string[5] = 's'
new_string = string[0:5] + 's'
print(new_string)













