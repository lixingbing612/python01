# break 用在循环体中，用来结束循环
for x in range(1,11,1):
    if x == 7:
        break
    print(x)

print('---------------------')

for y in range(1,11,1):
    print(y)
    if y == 7:
        break
# continue 用在循环体中，用来跳过循环
print('-----------------------')
for a in range(1,11,1):
    if a == 7:
        continue
    print(a)

print('----------------------')
for b in  range(1,11,1):
    print(b)
    if b == 7:
        break