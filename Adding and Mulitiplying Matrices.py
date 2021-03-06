# Matrices forms an important Mathematical concepts, with wider adoption
# In this Tutorial, the aim is demonstrating addition and multiplication of matrices 
# The below matrices, M1 and M2 are used for initial illustrations
M1 = [[8,14,-6],
        [12,7,4],
        [-11,3,21]]   
M2 = [[3, 16, -6],
        [9, 7, -4],
        [-1, 3, 13]]
# To print the matrix, we thus do the following operation
# print(M1) # This will print Matrix M1
# print(M2) # This will print Matrix M2
matrix_length1 = len(M1)  #The len operation counts the item numbers in the matrix
matrix_length2 = len(M2)
print("The Matrix of M1 is: ")
for i in range(matrix_length1): #In using the for function in this case, combined with len, prints the matrix in full
    print(M1[i])
print("The Matrix of M2 is:")
for i in range(matrix_length2):
        print(M2[i])
# The below matrices are created, for use in the computation process
M3 = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
M4 = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
# To add M1 and M2 matrix, we adopt the sum operator (+)
for i in range(len(M1)):
    for k in range(len(M2)):
        M3[i][k] = M1[i][k] + M2[i][k]
        # To multiply the M1 and M2 Matrices we adopt the multiplication operator ( * )
        M4[i][k] = M1[i][k] * M2[i][k]
# Here, to print the resulting matrices after adding and mu;ltiplying, we use the "print" funtion
print("The sum of Matrix M1 and M2 = ", M3)
print("The product of Matrix M1 and M2 = ", M4)