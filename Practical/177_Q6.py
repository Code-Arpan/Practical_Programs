D = ['Zero','One','Two','Three','Four','Five','Six',
                              'Seven','Eight','Nine']

n = int(input("Enter a digit(0-9): "))

if n in range(0,10):
    print(D[n])
else:
    print("Invalid Digit")