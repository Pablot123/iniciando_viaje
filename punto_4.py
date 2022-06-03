number_1 =10
number_2 =20
number_3 =6.5
# The error on the previus code was due to the precedence operator
# the division was first so at the begining the numer 3 was divided by 3 and later add  to the other two numbers
# to solve this i put a parentesis so the sum is made first and then the division
media =(number_1 +number_2 +number_3) /3 #Colocando los parentesis se realiza primero la suma de los tres numeros y luego la division
print(f"{media}es la nota media.")