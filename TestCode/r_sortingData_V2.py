
right_total = [[0 for col in range(2)] for row in range(16)]

k = 0
for i in range(4,8):
    for j in range(2):
        right_total[i][j] = oneSide[k][j]
    k+=1

k=4
for i in range(12,16):
    for j in range(2):
        right_total[i][j] = oneSide[k][j]
    k+=1




