def zero_striping(matrix):
    if not matrix or not matrix[0]:
        return
    
    zero_rows = set()
    zero_columns = set()

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == 0:
                zero_rows.add(row)
                zero_columns.add(column)
    
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if row in zero_rows or column in zero_columns:
                matrix[row][column] = 0

m = int(input("Enter number of rows in the matrix: ").strip())
print()
print("Now, enter the matrix:")
matrix = [[int(num) for num in input().strip().split()] for _ in range(m)]
# matrix = [[1,2,3,4,5],[6,0,6,9,10],[11,12,13,14,15],[16,17,18,19,0]]
zero_striping(matrix)
print()
print("Matrix after zero striping is: ")
for i in range(len(matrix)):
    print(" ".join(str(num) for num in matrix[i]))
# print(matrix)