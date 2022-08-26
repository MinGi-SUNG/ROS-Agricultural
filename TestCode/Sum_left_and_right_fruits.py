import random
for i in range(12):
    left_fruit = [[random.randrange(1,10)]*2 for i in range(12)]
    right_fruit = [[random.randrange(1,10)]*2 for i in range(12)]

# print(left_fruit)
# print(right_fruit)

for i in range(4):
    i=4+i
    left_fruit[i][0] = left_fruit[i][0] + left_fruit[15-i][0]
    left_fruit[i][1] = left_fruit[i][1] + left_fruit[15-i][1]
    del left_fruit[15-i]
left_fruit[4:8] = left_fruit[7], left_fruit[6], left_fruit[5], left_fruit[4]

# print(left_fruit)

for i in range(4):
    right_fruit[i][0] = right_fruit[i][0] + right_fruit[7-i][0]
    right_fruit[i][1] = right_fruit[i][1] + right_fruit[7-i][1]
    del right_fruit[7-i]
    
# print(right_fruit)

fruits = left_fruit[0:4] + right_fruit[0:4] + left_fruit[4:8] + right_fruit[4:8]

# print(fruits)

for i in range(16):
    for j in range(2):
        fruits[i][j] = str(fruits[i][j])

f = open("store_fruits_count.txt",'w')
f.write("tree_number / normal_fruit / disease_fruit\n")
for i in range(16):
    f.write(str(i+1)+" / "+fruits[i][0]+" / "+fruits[i][1]+"\n")
f.close()
