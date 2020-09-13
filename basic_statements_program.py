# code to print even number:

x = int(input("Enter a number: "))
for i in range(x + 1):
    if i % 2 == 0:
        print(str(i) + " -> Even number!")
