# print([x for x in range(1, 100) if x % 4 == 0])
# 具有特定的功能的代码块，比如登录功能
"""
def 函数名字（参数1，参数2...）：
    代码块
    return 具体值/默认是return None
"""
# 函数的定义：把具有独立功能的代码块组织成一个小模块，在需要是调用
'''
语法：
def 函数名():
    函数中的代码
    函数中的代码
1.def是关键字，用来定义函数的define的缩写
2.函数名需要遵循标识符的规则
3.处于def缩进中的代码，称为函数体
4.函数定义的时候，函数体中的代码不会执行，在调用是才会执行

def 函数名():
    pass        #代码中没有return时保存函数后续再使用
    return      #return后面没有数据时返回None
    return xx   #返回值xx
'''
def login():
    """这是一个定义的函数 按CTRL q 按CTRL b"""
    print('请输入账户:')
    print('请输入密码:')
    print('请输入验证码:')

#函数调用:
login()

#函数嵌套调用


def func1():
    print(1)
    print('func1')
    print(2)


def func2():
    print(3)
    func1()
    print(4)

print(5)
func2()
print(6)
# 1.位置参数
print('1.def定义一个加法函数名为add')


def add(x, y):
    z = x + y
    return z


print('--1+2', add(1, 2))
print('--a+b', add('a', 'b'))
result = add(100,299) #将求和的结果保存到变量result，可以在后续代码使用
print(result)

print('_'*20)

print('2.def可以一个函数定义多条结果值加减乘除')


def sql(x, y):
    add = x + y
    sub = x - y
    che = x * y
    chu = x / y
    return add, sub, che, chu


print(sql(4, 5))

# 2.关键字参数
print('3.def可通过.format定义关键字参数,key：value传递有多种方法')


def niao_chuang(name, age):
    a = '他叫{}，居然在{}岁之前就不尿床了！'.format(name, age)
    return a


print(niao_chuang('李狗剩', 17))
print(niao_chuang(name='王狗蛋', age=16))
print(niao_chuang(age=15, name='张铁柱'))
print(niao_chuang('二愣子', age=18))

print('4.def的默认参数就是直接在（）内输入值')
print(niao_chuang('大聪明', 17))


# #4.可变化参数，列表元组形式类似位置参数
print('5.def定义可变化参数，*args定义列表和元组形式的参数')
def add1(x,y,*args):
    z = x+y+sum(args)
    return z
print('--3,4,5就等于*(args)，要输入至少2个值', add1(1, 2, 3, 4, 5))
print('--返回x+y+所有(元组的元素)', add1(1,2,*(3,4,5)))    #传递多个参数
print('--返回x+y+所有[列表的元素]', add1(2,3,*[5,6,7,8]))     #传递列表

# #   b.变化参数,使用字典形式类似关键字参数
print('6.**args定义的是字典形式的参数')
def show_info(**kwargs):
    print(kwargs)
    return ' '
print(show_info(a='hello',b='world',c=123))

dt_data = {'x':1,'y':2,'z':3}
print(show_info(**dt_data))
#可以将可变参数列表和字典形式结合起来使用，此函数可以接收任何长度，任何位置，任何关键字的参数
def show_info1(*args,**kwargs):
    print(args,kwargs)
