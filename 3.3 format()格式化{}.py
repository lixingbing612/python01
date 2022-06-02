#格式化字符串 format格式多个参数：'{} {}'.format(参数1,参数2)
str1 = '今天周{}，张三用了{}元'.format('一', 99.9)
print('1.{}内的值为format的值：', str1)
#位置参数
str2 = '今天周{0}，张三用了{1}元'.format('一', 99.9)
print('2.{}内的数字为按照format内的值：', str2)
#关键字参数
str3 = '今天周{x}，张三用了{y}元'.format(x='一', y=99.9)
print('3.{}内的关键字对应foemat的值：', str3)
str4 = '今天周{x}，张三用了{0}元'.format(99.9, x='一')
print('4.{}可用数字也可用关键字：', str4)


# 字符串定义变量后 输出 f ‘{}’
name = 'zhangsan'
space = 'home'
print(f'我是{name},我在{space}')