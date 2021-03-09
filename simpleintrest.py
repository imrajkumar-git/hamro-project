 simpleInterest(P , R , N)
SI= (p*T*R)
return SI


P = float(input('Enter principal amount: '))
R = float(input('Enter the interest rate: '))
T = float(input('Enter time: '))

# calculate simple interest
SI = (P * R * T) / 100


# display result
print('Simple interest : {}'.format(SI ))
print('Total amount = ',( P + SI ))
