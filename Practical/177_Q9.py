sum = c = 0
print("Enter numbers:")
print("(Enter 'Q' to see the average)")

while True :
    n = input()
    if n == 'q' or n == 'Q' :
        break
    else :
        sum += int(n)
        c += 1

avg = sum / c
print("Average =",avg)