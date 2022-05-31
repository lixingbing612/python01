a = 7
b = 3
#算数运算符
print(a + b)    #7+3=10     加
print(a - b)    #7-3=4      减
print(a * b)    #7*3=21     乘
print(a / b)    #7/3=2.33333...     除
print(a // b)   #7/3=2（去除小数）    除取整
print(a % b)    #7/3=2+1取余数1      取余数
print(a ** b)   #7*7*7=343          幂
#比较运算符
print(a > b)    #7>3    大于
print(a >= b)   #7>=3   大等于
print(a < b)    #7<3    小于
print(a <= b)   #7<=3   小等于
print(a == b)   #7=3    等于
print(a != b)   #7<>3   不等于
print('============')
x = 12
y = 12
print(x is y)   #比较两个值的id地址是不是相等，当两个对象引用相同 条件：(-5~256)的整数、下划线、字母 的字符串 否则false
print(id(x))
print(id(y))
print(a is not b)   #比较两个值的id地址是不是相等 当两个对象引用不相同
#赋值运算符
a += b  #a=a+b          加赋值
print(a)    #3+7=10
a1 = 5
b1 = 8
a1 -= b1    #a1=a1-b1   减赋值
print(a1)   #5-8=-3
a2 = 4
b2 = 2
a2 *= b2    #a2=a2*b2   乘赋值
print(a2)   #4*2=8
a3 = 9
b3 = 3
a3 /= b3    #a3=a3/b3   除赋值
print(a3)   #9/3=3
a4 = 9
b4 = 5
a4 //= b4   #a4=a4//b4  取整赋值
print(a4)   #9/5=1（去除小数）
a5 = 3
b5 = 2
a5 **= b5   #a5=a5*a5   幂赋值
print(a5)   #3*3=9
a6 = 10
b6 = 4
a6 %= b6 #10/4=2取余数2    取余赋值
print(a6)
print('--------------------')
#逻辑运算符
c = 5
d = 10
# print(not True) #非，不对=错
print(not c<4)
print(not d>9)
# print(True and False)   #与，都为真时输出真
print(d>9 and c<6)
print(d>9 and c<4)
# print(True or False)    #或，其中有一个真时输出真
print(c>4 or d>11)
#优先级not>and>or True and not True or False --> (True and (not True)) or False --> (True and False) or False --> False or False --> False

