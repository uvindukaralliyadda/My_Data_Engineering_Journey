weight=input('Weight: ')
unit=input('(L)bs or (K)g: ')

if unit.upper() =='L':
    weigh=float(weight)*0.45
    print(f'{weigh}Kg')

else:
    converted=float(weight)/0.45
    print(f'{converted}Lbs')