i = 1

while i <= 10:
    print(i * '*')
    i += 1

names = ["John", "Bob", "Mosh", "Sam", "Mary"]
names[0] = "Jon"
print(names[0:3])

numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print(numbers)
print(len(numbers))

print('***************')
for item in numbers:
    print(item)

print('***************')
numbers = range(5, 10, 2)
for number in numbers:
    print(number)