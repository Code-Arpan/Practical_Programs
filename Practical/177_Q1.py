len = int(input("Enter length in centimetre: "))
if len < 0:
    print("Invalid input")
else:
    inch = len / 2.54
    print(len,"cm is equal to",inch,"inches")