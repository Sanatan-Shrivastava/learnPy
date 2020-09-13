word = "Marathon"

print(word[0]) #'M'
print(word[-1]) #'n'
print(word[0:]) #'arathon'
print(word[:-1]) #'Maratho'
print(word[1:-1]) #'aratho'

# strings are immutable in Python, hence you cannot manipulate strings in python.
word = "python tutorial"

# word[0] = S -> wrong [ use slice and concatenate ]
word = "s" + word[1:]
print('word after removing p, adding s is: ' + word) # that worked;

# length of the string:
# len() is an inbuilt function in python:
word = "sanatanshrivastava is my insta username"
print(len(word))
print(len(word[4:]))