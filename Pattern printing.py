n = int(input("Enter a number : "))
for i in range(n):
    for j in range(i):
        print(i, end=" ")
    print()

n = int(input("Enter a number : "))
for i in range(n):
    for j in range(i):
        print(j + 1, end=" ")
    print()

n = int(input("Enter a number : "))
for i in range(n):
    for j in range(i):
        print("*", end=" ")
    print()

n = int(input("Enter a number : "))
for i in range(1, n):
    for j in range(5 - i):
        print(i, end=" ")
    print()

n = int(input("Enter a number : "))
for i in range(1, n):
    for j in range(i, n):
        print(i, end=" ")
    print()


for i in range(1, 6):
    for j in range(1, 6):
        if j == 1 or i == 6 or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


n = int(input("Enter a number : "))
for i in range(1, n):
    for j in range(1, n):
        if j == 1 or i == n - 1 or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
