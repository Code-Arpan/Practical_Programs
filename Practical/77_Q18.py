cgos = int(input('Enter cost of goods sold: '))
rev = int(input('Enter revenue generated: '))
oc = int(input('Enter operating cost: '))

gp = rev - cgos     # Gross profit
np = gp - oc       # Net profit
npp = np/rev*100  # Net profit percentage

print('Gross profit =', gp)
print('Net profit =', np)
print('Net profit percentage =', npp,'%')