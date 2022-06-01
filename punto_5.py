#The following inputs takes the informaton about the grades(grade and percentage of the grade) of one person
first_grade = float(input('Enter first grade: '))
percentage_first_grade = float(input('Enter the percentage of the first grade: '))
second_grade = float(input('Enter second grade: '))
percentage_second_grade = float(input('Enter the percentage of the second grade: '))
third_grade = float(input('Enter third grade: '))
percentage_third_grade = float(input('Enter the percentage of the third grade: '))

final_grade = first_grade*(percentage_first_grade/100) + second_grade*(percentage_second_grade/100) + third_grade*(percentage_third_grade/100)

print(f'Your final grade is: {final_grade:.2f}') #i used .2f to print only two decimals