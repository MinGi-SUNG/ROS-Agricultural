import numpy as np

oneSide = [[0 for col in range(2)] for row in range(24)]
total = [[0 for col in range(2)] for row in range(16)]
Total_2 = [[0 for col in range(2)] for row in range(16)]
sortA = [[0 for col in range(3)] for row in range(16)]

#가상의 데이터 입력받은 배열
num=0
for col in range(len(oneSide)):
    for row in range(len(oneSide[col])):
        oneSide[col][row] = num
    num += 1

    
#REAL DATA SORTING START
#0-3번 과수 ,4-7 과수 왼쪽
for i in range(8):
    for j in range(2):
        total[i][j] = oneSide[i][j]

#8-11 과수 왼쪽
i=9
for k in range(8,12):
    for j in range(2):
        total[k][j] = oneSide[i][j]
    i+=2

#12-15번 과수
i = 17
for k in range(12,16):
    for j in range(2):
        total[k][j] = oneSide[i][j]
    i +=2

for i in range(0,8):
    for j in range(2):
        oneSide[i][j]=0

for j in range(2):
    oneSide[1][j] = oneSide[14][j]
    oneSide[3][j] = oneSide[12][j]
    oneSide[5][j] = oneSide[10][j]
    oneSide[7][j] = oneSide[8][j]
    oneSide[8][j] = oneSide[22][j]
    oneSide[9][j] = oneSide[20][j]
    oneSide[10][j] = oneSide[18][j]
    oneSide[11][j] = oneSide[16][j]

for i in range(12,24):
    for j in range(2):
        oneSide[i][j]=0

del oneSide[16:]

#과수 전체
Total_2 = [[c+d for c,d in zip(a,b)] for a,b in zip(oneSide, total)]


#과수 sorting
for i in range(12,16):
    sortA[i]=Total_2[i]

for i in range(8,12):
    j=11
    sortA[i]=Total_2[j]
    j -=1

k = 0
for i in range(0,8):
    if i%2==0:
        sortA[k]=Total_2[i]
        k+=1

k =4
for i in range(0,8):
    if i%2==1:
        sortA[k]=Total_2[i]
        k+=1

txtA = list(map(str,sortA))


#과수 배열 txt 정리하기

file = open("ex2.txt",'w')
for i in range(0,16):
    file.write(txtA[i])
    file.write("\n")

f = open('ex.txt', 'w')
for i in range(0,16):
        data = "%dth\n" % (i+1)
        f.write(data)

final = open('fruitData.txt','w')
f = open('ex.txt','r')
file = open('ex2.txt','r')
for i in range(0,16):
    a= f.readline()
    b= file.readline()
    final.write(a)
    final.write(b)


final.close()
f.close()
file.close()
