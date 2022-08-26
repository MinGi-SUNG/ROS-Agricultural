for i in range(12):
    cnt_left = [[i]*2 for i in range(12)]
    cnt_right = [[i]*2 for i in range(12)]

for i in range(4):
    i=i+4
    cnt_left[i][0] = cnt_left[i][0] + cnt_left[15-i][0]
    cnt_left[i][1] = cnt_left[i][1] + cnt_left[15-i][1]
    del cnt_left[15-i]

print(cnt_left)

for i in range(4):
    cnt_right[i][0] = cnt_right[i][0] + cnt_right[7-i][0]
    cnt_right[i][1] = cnt_right[i][1] + cnt_right[7-i][1]
    del cnt_right[7-i]

print(cnt_right)

fruits = cnt_left[0:4] + cnt_right[0:4] + cnt_left[4:8] + cnt_right[4:8]

print(fruits)
