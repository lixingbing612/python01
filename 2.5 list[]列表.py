# 列表
# 格式：变量名=[]
alit = ['pink', 'pink', 'write']
print(alit)
# 循环列表
for x in alit:
    print('列表中的元素', x)

#列表的使用方法

alit.append('black')
print('1.添加元素black', alit)

print('2.统计pink元素出现次数', alit.count('pink'))

alit.extend(['red'])
print('3.末尾追加元素red', alit)

print('4.匹配black第一个的位置', alit.index('black'))

alit.insert(1, 'blue')
print('5.按位置1插入blue元素', alit)

alit.pop(3)
print('6.删除位置3的元素write，默认是最后一个', alit)
#print(alit.pop(3)) 删除元素并返回该元素

alit.remove('pink')
print('7.移除元素pink的第一个', alit)

alit.reverse()
print('8.反向列表元素顺序', alit)

alit.sort()
print('9.对列表排序', alit)

blit = alit.copy()
print('10.复制列表到新表', blit)

alit.clear()
print('11.清空列表alit的元素', alit)