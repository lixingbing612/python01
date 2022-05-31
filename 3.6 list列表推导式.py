#列表推导式：【表达式2  循环体  表达式1】，执行的顺序：先执行循环体，其次表达式1，最后表达式2

#生成1-10的列表
lst = []
for x in range(1,11):
    lst.append(x)
print(lst)
print('列表推导式格式为：[表达式2 循环体 表达式1],')
print('[x for x in range(1, 11)]', [x for x in range(1, 11)])
#生成1-10，打印奇数
print('生成1-10，打印奇数', [x for x in range(1, 11) if x % 2 != 0])
print('生成1-10，打印奇数', [x for x in range(1, 11) if x % 2])
#生成1-10，打印奇数,基础上加10
print('生成1-10，打印奇数基础上加10', [x+10 for x in range(1, 11) if x % 2 != 0])

lst1 = [x for x in range(0, 10) ] #1.for循环后无表达式
lst2 = [x for x in range(0, 10) if x % 2 == 0] #2.for循环后if条件表达式
lst3 = [x*2+1 for x in range(0, 10) if x % 2 == 0] #3.返回的值参与计算
lst4 = [y+str(x) for x in range(1, 3) for y in ['x', 'y', 'z']] #4.嵌套循环
print("生成0~9的列表：", lst1)
print("对0~9的数对2取余返回新列表：", lst2)
print("对0~9的数对2取余后再参与计算:", lst3)
print("嵌套循环生成的数相连接：", lst4)