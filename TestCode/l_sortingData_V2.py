xtA = [[c+d for c,d in zip(a,b)] for a,b in zip(left_total, r_sortingData_V2.right_total)]
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
