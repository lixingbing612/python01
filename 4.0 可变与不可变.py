my_list = [1,2,3]
my_list1 = [1,2,3]

print('mylist:',id(my_list))        #列表引用的地址
print('mylist1:',id(my_list1))      #列表引用的地址
print('mylist:',id(my_list),id(my_list[1]))

my_list[1] = 10     #改变的是列表中下标为1的位置引用
print(my_list)
print('mylist:',id(my_list)) #列表的引用没有变化
print('mylist:',id(my_list),id(my_list[1])) #列表的位置1的引用变化

print('-'*20)
my_tuple = (1,2,[3,4]) #元组中存储的是1的地址，2的地址，和列表的地址
#元组中的数据不能改变，是值 1，2，[]这三个地址不能改变
print(my_tuple,id(my_tuple[-1]))
my_tuple[-1][0] = 10
print(my_tuple,id(my_tuple[-1]))

#只有 = ，才可以改变引用
#可变类型做参考，再函数内部如果不适用 = 直接修改形参的引用面 对形参进行的数据修改会同步到实参数中


# 交换两个变量的值
a = 10
b = 20

a,b = b,a
print(a,b)

#组包：将多个数据值使用逗号连接 组成元组
c = b, a #组包
print(type(c),c)
#拆包：将容器中的数据值使用多个变量分别保存的过程，注意变量的个数和容器中数据个数要保持一致
a, b = c
print(a,b)

#赋值运算符都是先执行 = 右边的代码，执行结果保存到 = 左边的变量中