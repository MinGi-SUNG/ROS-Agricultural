import numpy as np

right_total = [[0 for col in range(2)] for row in range(16)]
oneSide = [[0 for col in range(2)] for row in range(12)]

#가상의 데이터 입력받은 배열
num=0
for col in range(len(oneSide)):
    for row in range(len(oneSide[col])):
        oneSide[col][row] = num
    num += 1


k = 7
for i in range(0,4):
    for j in range(2):
        oneSide[i][j] +=oneSide[k][j]
    k-=1

del oneSide[4:8]


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

#왼쪽 오른쪽 txt 만들어서 새 파일에서 한줄씩 합쳐서 저장하기



