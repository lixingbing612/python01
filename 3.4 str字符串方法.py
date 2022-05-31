# #字符串常用方法
str1 = '-'
str2 = str1.join('world')
print('1.将字符str1的值插入str2的每个值中间达成分割', str2)

str3 = 'hello my dear python java php'
print('2.在字符str3中找到空格位置进行截断并输出', str3.split(' '))

print('3.检查字符str3是否有python，返回开始的索引值', str3.find('python'))
print('---str3字符中没有k，返回-1', str3.find('k'))
print('---index也可以检查有无搜索的元素，当没有时报错', str3.index('python'))

str4 = 'internet young'
print('4.返回str4字符的长度', str4, len(str4))

print('5.判断str3字符是否以hello开头', str3.startswith('hello'))

print('6.判断str4字符是否以old结尾', str4.endswith('old'))

print('7.替换str4中重复的young为swim', str4.replace('young', 'swim'))

print('8.isdigit字符只包含数字', 'isalpha字符只包含字母', 'isnumeric字符只包含数字', 'isspace字符只包含空格', )
for str5 in '123':
    if str5.isdigit():
        print(str5, end=' ')
str6 = 'ASS57Dyzk13'
print('9.返回字符str5中最大的字符（min返回最小）', max(str6))

print('10.lower()将字符的所有大写转换小写，upper（）小写转大写')