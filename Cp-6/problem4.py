a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
d = int(input("Enter the number: "))

if a > b and a > c and a > d:
    print("a is greater")
elif b > a and b > c and b > d:
    print("b is greater")
elif c > a and c > b and c > d:
    print("c is greater")
else:
    print("d is greater")
