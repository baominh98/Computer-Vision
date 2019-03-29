n = int(input('Nhap So Luong Phan Tu:'))
inputArray = []
for i in range(n):
    inputArray.append(float(input('Phan Tu Thu %d: '%(i+1))))
print(inputArray)
min=float(inputArray[0])
max = float(inputArray[0])

for i in inputArray:
    if i <min:
        min=i
    if i>max:
        max = i

# for i in range(n):
#     if inputArray[i] <min:
#         min=inputArray[i]
#     if inputArray[i]>max:
#         max = inputArray[i]
print('Min: ' + str(min) + ' | Max: ' + str(max))