#Slicing
matriz =[[2, 4, 3, 6],[8, 3, 4, 5],[7, 1, 3, 10],[9, 2, 1, 4]]
print(matriz)
slicing_method = matriz

#for the slicing the strategy was change the last number of each row by the sum
#for the sum we take the first 3 elements of each row using [0:3]
slicing_method[0][-1] = sum(slicing_method[0][0:3]) 
slicing_method[1][-1] = sum(slicing_method[1][0:3])
slicing_method[2][-1] = sum(slicing_method[2][0:3])
slicing_method[3][-1] = sum(slicing_method[3][0:3])
print(slicing_method)

#Append
# to use append i pop the last element of each array and then use append with the sum
matriz =[[2, 4, 3, 6],[8, 3, 4, 5],[7, 1, 3, 10],[9, 2, 1, 4]]
append_method = matriz

#For the append the strategy was first pop the last element of each row and the append the sum of the list
# resulting after the pop
append_method[0].pop(-1)
append_method[0].append(sum(append_method[0]))
append_method[1].pop(-1)
append_method[1].append(sum(append_method[1]))
append_method[2].pop(-1)
append_method[2].append(sum(append_method[2]))
append_method[3].pop(-1)
append_method[3].append(sum(append_method[3]))


print(append_method)
