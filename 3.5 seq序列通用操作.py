#序列的通用操作
# 1.序列索引（列表，元组，字符串）
# 索引：seq[index] ,index 代表下标，默认是从0开始
lst = ['一', '二', '三', '四', '五', '六']
print('1.返回列表lst的第[]个元素', lst[1])

tp = ('一', '二', '三', '四', '五', '六')
print('--返回元组tp位置-1的元素', tp[-1])

a = '一二三四五六七八九十'
print('--返回字符串a位置3的元素', a[3])

#2.序列的切片:seq[start:end:step] （列表，元组，字符串）
# start代表位置，默认0，end:代表结束位置，如不填写则代表列表长度，step代表的是步长，默认1
print('2.返回列表lst的2-5位的元素', lst[1:5:1])
print('--返回列表lst的偶数位的元素', lst[1:6:2])
print('--相当于print(lst[0:6:2]', lst[::2])
print('--相当于 print(lst[2:6:1])', lst[2::])
print(lst[2:])
print(lst[:5:])
print(lst[1::2])
print(lst[::2])

print('--元组也可以切片', tp[1:5:2])

print('--字符串也可以切片', a[1:7:2])

# #3.序列的相加相乘：+ *（列表，元组，字符串）
lst1 = [1, 2, 3, 4, 5]
lst2 = lst + lst1
print('3.将列表lst和lst1相加', lst2)

lst3 = lst1 * 2
print('--将列表lst1的值*2', lst3)

# #4.检查元素 in/not in（列表，元组，字符串）
print('4.判断元素1在列表lst1', 1 in lst1)
print('--判断元素2不在列表lst1', 2 not in lst1)

print('5.返回列表lst1最大值', max(lst1))
print('--返回列表lst1最小值', min(lst1))
print('--返回列表lst1求和', sum(lst1))
print('--对列表lst1排序', sorted(lst1))
# print(reversed([12345]))
print('返回列表lst1的长度', len(lst1))

# #序列中的方法：转化成列表  list()
# lst = []
p = 'abc'
lst4 = list(p)
print('6.将字符串p转换成列表', p, lst4)

# # 转化成字符串 str()
alst = [1,2,4,]
astr = str(alst)
print('--将列表alst转换成字符astr', astr)

# #循环列表
print('7.返回列表lst0的元素，end为循环到每个元素时加上end的值', )
lst0 = ['a', 'b', 'c', 'd']
for x in lst0:
    print(x, end='*')
print(' ' * 20)

# #循环序列中的索引和值
print('8.enumerate将序列组合成一个索引序列')
for x, y in enumerate(lst0):
    print(x, '====', y)