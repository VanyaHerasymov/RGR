import random

row = 5
col = 5
i=0
j=0
matrix=[]
row_matrix=[]
for i in range(row) :
    for j in range(col):
        
        rand = random.randint(1,9) 
        row_matrix.append(rand)
        print(rand, end=" ")
    matrix.append(row_matrix)
    row_matrix=[]
    print()


print()
print()

def ReverseMatrix90(matrix):
    for i in range(row):
        for j in range(col):
            print(matrix[row-j-1][i], end=" ")
        print()

ReverseMatrix90(matrix)