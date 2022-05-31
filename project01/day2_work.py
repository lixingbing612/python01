# 1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
a = int(input('请输入a的值'))
b = int(input('请输入b的值'))
c = int(input('请输入c的值'))
d = int(input('请输入d的值'))
print(a+b-c*d)

print('----------------------------------------------------')

# 2. 打印1~100内被3整除的所有数的和 。
s = 0
for x in range(1, 100, 1):
    if x % 3 == 0:
        s += x
        print(x)
s1 = 0
for x in range(3,101,3):
    s1 += x
    print(s1)

s2 = 0
x = 1
while x <= 100:
    if x% 3 ==0:
        s2 += x
        x += 1
        print(s2)

print('----------------------------------------------------')

# 3. 使用range()输出1~10内的所有奇数 。
for x in range(1, 10, 2):
    print(x)

print('----------------------------------------------------')

# 4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
sum1 = 0
sum2 = 0
for x in range(2, 100, 2):
    sum1 += x
for y in range(1, 100, 2): #这行可以用else:
    sum2 += y
print(sum1-sum2)

print('----------------------------------------------------')

# 5. 求1+2+3+...+100的和
sum = 0
a = 1
while a <= 100:
    sum += a
    a += 1
    print(sum)

sum1 = 0
for x in range(1,101):
    sum1 += x
    print(sum1)

print('----------------------------------------------------')

# 6. 判断一个数n能同时被3和5整除
n = int(input('请输入要判断的数字'))
if n % 3 == 0 and n % 5 == 0:
    print('这个数可以同时被3和5整除')
else:
    print('这个数不可以同时被3和5整除')

print('----------------------------------------------------')

# 7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
x = int(input('请输入要判断的数字'))
if x in range(101):
    print(x)

x1 = input('请输入要判断的数字')
if 1 < int(x1) < 100:
    print(x1)
print('-----------------------------------------------------')

# 8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
x = input('输入整数x:')
y = input('输入整数y:')
z = input('输入整数z:')
lst = [x, y, z]
print(lst)
lst.sort()
print(lst)

x = int(input("请输入整数x: "))
y = int(input("请输入整数y："))
z = int(input("请输入整数z: "))
if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y
print(x, y, z)

print('-----------------------------------------------------')

# 9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。备注：需要使用input()方法
score = int(input('请输入成绩'))
if score >= 90:
    print('A')
elif 60 < score <89:
    print('B')
else:
    print('C')

print('-----------------------------------------------------')

# 10. 将一个列表的数据复制到另一个列表中。
lst1 = [1, 34, 'sd', None]
lst2 = ['aa', 'bb', 'cc']
lst1.extend(lst2)
print(lst1)

print('-----------------------------------------------------')

# 11. 输出 9*9 乘法口诀表。
for x in range(1, 10):
    for y in range(1, x+1):
        print(y, '*', x, '=', x * y, end=' ')
    print()

print('-----------------------------------------------------')

# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
a = input('输入一行字符')
zf = 0
spc = 0
num = 0
other = 0
for x in a:
    if x.isdigit():
        zf += 1
    elif x.isdigit():
        num += 1
    elif x.isspace():
        spc += 1
    else:
        other += 1
print('字符', zf, '数字', num, '空格', spc, '其他', other)

print('-----------------------------------------------------')

# 13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
a = int(input('请输入数字'))
b = int(input('请输入相加个数'))
s, s_sum = 0, 0
for x in range(b):
    s += a * 10 ** (x)
    s_sum += s
    print(s_sum)

print('-----------------------------------------------------')

# 14. 题目：打印出如下图案（菱形）:
x = '*'
for i in range(1, 8, 2):
    print((x * i).center(7))
    for i in reversed(range(1, 6, 2)):
        print((x * i).center(7))
# 14. 题目：打印出如下图案（菱形）:
"""
上面的循环：
n=1 3 + 1 + 3
n=2 2 + 3 + 2
n=3 1 + 5 + 1
n=4 0 + 7 + 0

space = ' ' * (x-n)
star = '*' * (2 * (n-1) + 1)

下面的循环：
n=1 1+5
n=2 2+3
n=3 3+1
space=' ' * n
star='*' * (5-(n-1)*2)

"""
num = 5     #总数
x = num - 1 #循环轮次
for n in range(1, num):
    space = ' ' * (x-n)
    star = '*' * (2 * (n-1) + 1)
    print(space + star)
    # print(space + star + space)

for n in range(1,4):
    space = ' ' * n
    star = '*' * (5 - (n - 1) * 2)
    print(space + star)

for i in range(1, 8, 2):
    str = '*' * i
    print(str.center(7))
for i in range(5, 0, -2):
    str = '*' * i
    print(str.center(7))

star1 = '*'
a = [1,3,5,7,5,3,1]
for i in a:
    print((star1*i).center(7))
