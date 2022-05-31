'''
条件语句 if
if 该条件为真:
执行的代码块
'''

a = 10
if a > 13:
    print('a是大于13的数')
else:
    print('a是小于13的数')
#多条件判断
#有多个elif时最后要有一个else结束
score = 75
if score > 90:
    print('优秀')
elif score > 80:
    print('良')
elif score > 60:
    print('及格')
else:
    print('不及格')

if score > 75 and score < 90:
    print('良')

# 各数据类型的返回值
# 数字或浮点数，0或0.0返回False,其它值返回True
if 1:
    print('hello world')
if 0:
    print(111)
# 字符串，对于空字符串为返回False，其它值返回True
if '':
    print('haha')
if 'a':
    print('heihei')
# None，对于None返回False,非None值为True
if None:
    print('what the fuck')

# 列表|元组|字典，对于空列表，空元组，空字典都是返回False，非空值返回True

# in : 判断前面的元素在后面的对象中
a1 = '我是一个字符串'
b1 = '我是'
if b1 in a1:
    print("在字符串内")
else:
    print("不在字符串内")
