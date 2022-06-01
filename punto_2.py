
users =[]

#The for code is to take the information from the three users 
print('INFORMATION USER #1')
name_complete_user_1 = input('Please enter your complete name: ')
ocupation_user_1 = input('Please enter your ocupation: ')
age_user_1 = int(input('Please enter you age: '))
city_user_1 = input('Please enter your city: ')
number_user_1 = input('Please enter your number: ') #numer can contain special characters like '-' or '+'
email_user_1 = input('Please enter your email: ')
#Here we save the information from each user in a tuple(inmutable colection structure)
users.append((name_complete_user_1, ocupation_user_1, age_user_1, city_user_1, number_user_1, email_user_1))
print('\n') # used to show a space between each user

print('INFORMATION USER #2')
name_complete_user_2 = input('Please enter your complete name: ')
ocupation_user_2 = input('Please enter your ocupation: ')
age_user_2 = int(input('Please enter you age: '))
city_user_2 = input('Please enter your city: ')
number_user_2 = input('Please enter your number: ') #numer can contain special characters like '-' or '+'
email_user_2 = input('Please enter your email: ')
#Here we save the information from each user in a tuple(inmutable colection structure)
users.append((name_complete_user_2, ocupation_user_2, age_user_2, city_user_2, number_user_2, email_user_2))
print('\n') # used to show a space between each user

print('INFORMATION USER #3')
name_complete_user_3 = input('Please enter your complete name: ')
ocupation_user_3 = input('Please enter your ocupation: ')
age_user_3 = int(input('Please enter you age: '))
city_user_3 = input('Please enter your city: ')
number_user_3 = input('Please enter your number: ') #numer can contain special characters like '-' or '+'
email_user_3 = input('Please enter your email: ')
#Here we save the information from each user in a tuple(inmutable colection structure)
users.append((name_complete_user_3, ocupation_user_3, age_user_3, city_user_3, number_user_3, email_user_3))
print('\n') # used to show a space between each user
users = tuple(users)
print(f'Information user 1: {users[0]}\nInformation user 2: {users[1]}\nInformation user 3: {users[2]}')