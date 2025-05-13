numbers=[5,2,1,7,4]
numbers.append(20)

print(numbers)

numbers.insert(0,10)
print(numbers)

numbers.remove(5)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.index(2))

print(50 in numbers)

print(numbers.count(7))

print(numbers.sort())

numbers2=numbers.copy()
print(numbers2)

for x in numbers:
    print(numbers.pop())