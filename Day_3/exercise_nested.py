numbers =[5,2,5,2,2]

for item in numbers:
    print('x' * item)

for x in numbers:
    output= ''
    for count in range(x):
        output+='x'
    print(output)