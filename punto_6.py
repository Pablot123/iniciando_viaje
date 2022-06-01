#Slicing
matriz =[[2, 4, 3, 6],[8, 3, 4, 5],[7, 1, 3, 10],[9, 2, 1, 4]]
print(matriz)
prueba = matriz

prueba[0][-1] = sum(prueba[0][0:3])
prueba[1][-1] = sum(prueba[1][0:3])
prueba[2][-1] = sum(prueba[2][0:3])
prueba[3][-1] = sum(prueba[3][0:3])
print(prueba)

#Append
# to use append i pop the last element of each array and then use append with the sum
matriz =[[2, 4, 3, 6],[8, 3, 4, 5],[7, 1, 3, 10],[9, 2, 1, 4]]
prueba_2 = matriz

prueba_2[0].pop(-1)
prueba_2[0].append(sum(prueba_2[0]))
prueba_2[1].pop(-1)
prueba_2[1].append(sum(prueba_2[1]))
prueba_2[2].pop(-1)
prueba_2[2].append(sum(prueba_2[2]))
prueba_2[3].pop(-1)
prueba_2[3].append(sum(prueba_2[3]))


print(prueba_2)
