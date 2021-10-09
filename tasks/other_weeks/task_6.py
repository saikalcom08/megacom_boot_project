a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))

if a % b == 0:
    print(f"{a} can be deleted to {b} without remainder")
else:
    print(f"{a} can't be deleted to {b} wholly")