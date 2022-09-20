n = int(input("Enter number of items: "))
cost = 0

if n >= 100 :
    cost = n * 70
elif n >= 10 :
    cost = n * 100
else :
    cost = n * 120

print("Total Cost =", cost)