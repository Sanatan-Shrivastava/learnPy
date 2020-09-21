"""
---------------- functions in strings ------------------
*** difference between Character and String:

Character is one character. String is zero or more characters.
for eg,
char c = 'a';  
String s = "Hi!";
Note the single quotes for character, and double quotes for String.

** Two ways to pass string into the function: 

[*] -> str.function(<string_name>)
[*] -> <string_name>.function()
"""
# declare a string:
string = "Hello World"

# Convert whole string into uppercase
print(string.upper())
print(str.upper(string))

# Capitalize -> Turn first charcater into capital and rest as small:
print(str.capitalize(string))
print(string.capitalize())

# Convert whole string into lowercase
print(string.lower())
print(str.lower(string))

# SwapCase:
string_b = "WHARTON"
print(string_b.swapcase())
print(str.swapcase(string_b))


# Count the number of occurences of particular character in a string:
string_b = "MINNEAPOLIS"
ch = 'N'
a = string_b.count(ch)
print(a)

string_c = "Sanatan Shrivastava"
# Replace() -> Replace string with another string:
print(string_c.replace("Shrivastava", "Sharma"))
print(string_c.replace(string_c[0:7], "Akanksha"))

# startsWith(): -> boolean
print(string_c.startswith(''))

# endsWith(): -> boolean
print(string_c.endswith('A'))

# find() -> find the index of a character in a given string.
# syntax: <string_name>.find(string)
print(string_c.find('S'))

string_d = "This is a name"
list_string = string_d.split(' ')
print(list_string)

"""
numeric -> '1','2','3'
aplhabetic -> 'o','b','c'
alphanumeric -> "s2f24cda4214"
"""
# to find if the given string is numeric or not:
string_numeric = "3233232"
print(str.isnumeric(string_numeric))
print(string_numeric.isnumeric())

# to find if the given string is alphabetic or not:
string_alpha = "dsddreredede"
string_a

# to find if the given string is aplhanumeric or not: