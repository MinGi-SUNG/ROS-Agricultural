import numpy as np

import r_sortingData_V2

left_total = [[0 for col in range(2)] for row in range(16)]
oneSide = [[0 for col in range(2)] for row in range(12)]

#가상의 데이터 입력받은 배열
num=0
for col in range(len(oneSide)):
    for row in range(len(oneSide[col])):
        oneSide[col][row] = num
    num += 1


k = 11
for i in range(4,8):
    for j in range(2):
        oneSide[i][j] +=oneSide[k][j]
    k-=1

del oneSide[8:]

for i in range(0,4):
    for j in range(2):
        left_total[i][j] = oneSide[i][j]

for i in range(8,12):
    for j in range(2):
        k=7
        left_total[i][j] = oneSide[k][j]
        k-=1

txtA = [[c+d for c,d in zip(a,b)] for a,b in zip(left_total, r_sortingData_V2.right_total)]
Total = list(map(str,txtA))

file = open("ex3.txt",'w')
for i in range(0,16):
    file.write(Total[i])
    file.write("\n")

f = open('ex4.txt', 'w')
for i in range(0,16):
        data = "%dth normal|disease \n" % (i+1)
        f.write(data)

final = open('fruitData.txt', 'w')
f = open('ex3.txt', 'r')
file = open('ex4.txt', 'r')
for i in range(0, 16):
        a = f.readline()
        b = file.readline()
        final.write(b)
        final.write(a)

final.close()
f.close()
file.close()