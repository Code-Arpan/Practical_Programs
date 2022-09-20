basic= float(input("Enter Basic Salary :"))
hra_per = float(input("Enter hra% :"))
da_per = float(input("Enter da% :"))
tax_per = float(input("Enter tax% :"))

hra = float(basic*(hra_per/100))
da = float(basic*(da_per/100))
tax = float(basic*(tax_per/100))

net_salary = basic + hra + da - tax
print("Net Salary =",net_salary)


