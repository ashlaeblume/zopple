l1 = [0, 0]
l2 = [0, 0]
newboard = [l1, l2]
print(newboard)
newboard[0][0] = 5
print(newboard)


m, n = 4, 4

col_ex_1 = [[None for j in range(n)] for i in range(m)]
col_ex_2 = [[None]*n for i in range(m)]

print(col_ex_1)
print(col_ex_2)


for i in range(m):
    row = []
    col = []
    for j in range(n):
        row.append(None)
    print(row[0])

twodlist = [[row.append(None) for j in range(n)] for i in range(m)]
