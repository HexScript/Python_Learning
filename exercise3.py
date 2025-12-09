weight = input("Weight: ")
unit = input("(K)g or (L)bs: ")
converted = 0

if unit == 'K' or unit == 'k':
    converted = float(weight) * 2.20462
    print(f'Weight in Lbs: {converted}')
elif unit == 'L' or unit == 'l':
    converted = float(weight) / 2.20462
    print(f'Weight in KG: {converted}')
else:
    print('Error Error!!!')