#字符串str
#   格式化符号%
#格式化字符串
str1 = '它的名字叫%s' % '张三'
print('1.%s格式化字符串张三', str1)

str2 = '张三今年%d岁' % 22.2
print('2.%d格式化整数22.2', str2)

str3 = '张三今天用了%f元' % 99.9
print('3.1 %f格式化浮点数99.9', str3)

str4 = '张三今天用了%8.2f元' % 99.9
print('3.2 %8.2f：8是打印宽度，2是小数点位', str4)

str5 = '它的名字叫%8s哦' % '0张三0'
print('3.2.1 字符串也可以改宽度', str5)

str6 = '张三今天用了%-7.2f元' % 99.9
print('3.3 左对齐', str6)

str7 = '张三今天用了%+-7.2f元' % 99.9
print('3.4 数字前面显示+号', str7)

str8 = '张三今天用了% -7.2f元' % 99.9
print('3.5 数字前面显示空格', str8)

str9 = '一斤苹果%07.3f元' % (9.345)
print('3.6 数字前面显示0', str9)