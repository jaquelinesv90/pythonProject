for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

numbers = [5,2,5,2,2]
for count in numbers:
    print('x' * count)

names = ['John','Bob','Lucie','Sarah','Marie']
print(names[2:3])

numbers = [3,7,9,1]
largest_number = 0
for number in numbers:
    if number > largest_number:
        largest_number = number
print(largest_number)

numbers = [2,2,2,2,5]
for count in numbers:
    print('x' * count)

numbers2 = [5,2,1,7,4]
numbers2.insert(2,8)
print(numbers2)

number1 = 5
number2 = 4
print("the sum are ",number1+number2)

number1 = 5
number2 = 4
number3 = 8
number4 = 10
average = (number1 + number2+number3+number4)/4
print("average ",average)

number1 = -9
if number1 > 0:
    print("positive number")
else:
    print("negative number")