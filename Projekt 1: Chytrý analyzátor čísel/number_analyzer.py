'''input'''
user_numbers = []
while True:
    user_input = input('Insert a number and cancel with "done":')
    if user_input == 'done':
        break
    elif user_input is str or user_input is int:
        int_user_input = int(user_input)
        user_numbers.append(user_input)
    else:
        print('Invalid input')

'''all numbers'''
for number in user_numbers:
    print(number)
print(f'all inserted numbers as list: {user_numbers}')
mylist = ', '.join(user_numbers)
print(f'numbers inserted are {mylist}')

'''suma'''
suma = 0
for number in user_numbers:
    int_number = int(number)
    suma += int_number
print(f'total sum of inserted numbers is {suma}')

'''prumer'''
mean = suma / len(user_numbers)
print(f'mean is {mean}')

'''sudy/lichy'''
even=0
odd=0
for number in user_numbers:
    int_number = int(number)
    if int_number % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'number of even numbers is {even}')
print(f'number of odd numbers is {odd}')
