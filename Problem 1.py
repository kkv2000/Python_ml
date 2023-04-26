n = int(input("Enter a number"))
if n % 2 != 0:
    print (" weird")
elif n % 2 == 0:
    if n in range (2,6):
        print (" not weird")
    if n in range (6,21):
        print("weird")
    if n > 20:
        print("not weird")
