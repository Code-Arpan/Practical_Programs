p = int(input('Enter Principal Loan Amount : '))
r = int(input('Enter annual rate of interest : '))/1200
n = int(input('Enter tenure of loan repayment : '))

print('EMI =', p*r*pow((1+r), n)/(pow((1+r), n)-1))