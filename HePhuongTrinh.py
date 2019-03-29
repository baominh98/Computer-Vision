for i in range(4000, 5301):
    temb = 0
    for j in range(1, i + 1):
        if i % j == 0:
            temb = temb + 1
    if temb == 2 or temb == 1:
        print('So Nguyen To: ' + str(i))
#
# count = 0
# wc = 0
# with open('D:\Log.txt') as f:
#     for line in f:
#         count = count + 1
#         wc = wc + len(line.split(' '))
# print(wc, count)