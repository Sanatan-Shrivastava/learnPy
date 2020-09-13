
# if statement in python:

x = int(input("Please enter the number: "))

if x < 9:
    print("One digit number")
elif x >= 10 and x <= 99:
    print("Two digit number")
else:
    print("More than two digit number")


# for statements:

x = int(input("Enter the number: "))
for i in str(x):
    print (i)

for i in range(0, len(str(x))):
    print (i)

for i in range(0, x + 1):
    print (i)

for i in range(x + 1):
    print (i)


# code to print sum of 'n' natural numbers:
print("Sum of first n natural numbers is: " + str(sum(range(int(input("Enter the number: ")) + 1))))
print(range(0,10,3))


# printing given list:

a = [1,2,3,4,6]
for i in range(len(a)):
    print(i, a[i])

# printing given list:

b = ['Mary', 'John', 'Alex', 'Prime']
age = [20, 10, 30, 40]
for i in range(len(b)):
    print (b[i] + " - " + str(age[i]))
