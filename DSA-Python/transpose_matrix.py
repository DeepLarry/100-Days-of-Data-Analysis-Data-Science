n=int(input("Enter the number of rows: "))
m=int(input("Enter the number of columns: "))
matrix=[]
print("Enter the elements of the matrix:")
for i in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
transpose=[[0 for j in range(n)] for i in range(m)]
for i in range(n):
    for j in range(m):
        transpose[j][i]=matrix[i][j]
print("Transpose of the matrix:")
for i in range(m):
    for j in range(n):
        print(transpose[i][j],end=" ")
    print()
