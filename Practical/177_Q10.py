print("Enter numbers:")
print("(Enter 'Q' to see the result)")
lar = 0

while True :
    n = input()
    if n == 'Q' or n == 'q' :
        break
    else :
        lar = max(lar,int(n))

print(lar, "is the largest number")