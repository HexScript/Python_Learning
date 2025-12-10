course = 'Python for beginners'
x = 0
temperature = 5

print(course.find('y'))
print(course.replace('for', '4'))
print('Python' in course)

x += 3
print(x)
x *= 3
print(x)

if temperature > 30:
    print('Oh its hot!')
    print('Drink Drink!')
elif temperature > 20:
    print("Medium temperature")
elif temperature > 10:
    print('Its getting cold!')
else:
    print('Cold Zero!')
    print('Get more clothes!!!')
