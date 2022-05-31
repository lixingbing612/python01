#字典 字典是一种无序的，可变的序列，它的每组元素都有键值对组成，中间用冒号分隔，如果有多组元素的话，元素与元素用逗号隔开
#格式：变量名 = {key1:value1 , key2:value2}
dic1 = {'name':'张三','sex':'男','city':'北京'}
print(dic1)

## 字典 字典是无序可变的序列，每组元素都有键值对组成，中间用冒号分隔，如果有多组元素时用逗号隔开
# 格式：变量名 = {key1:value1 , key2:value2}

d1 = {'zhangsan': 23, 'lisi': 19, 'wangwu':31, 'zhaoliu':42}
print('1.创建字典d1',d1)

print('2.获取字典d1中的lisi键值',d1['lisi'])

d1['lisi'] = '29'
print('3.更新字典d1中lisi的键值', d1)

d2 = {}
d2.update(d1)
print('4.更新字典d1的值到字典d2', d2)

print('5.判断字典d2是否存在键名lisi', 'lisi' in d2)

print('6.获取字典d2的所有键名', d2.keys())
for x in d2.keys():
    print('字典d2的键名', x)

print('7.获取字典d2的所有键值', d2.values())
for x in d2.values():
    print('字典d2的键值', x)

print('8.获取字典d2的所有键值对', d2.items())
for x in d2.items():
    print('字典d2的键值对', x)
for x, y in d2.items():
    print('字典d2的键值对', x, '=========', y)

d3 = d2.copy()
print('9.拷贝字典d2到d3', d3)

print(d1.clear())
print('10.删除d1的所有元素', d1)

print('11.删除字典d3中zhangsan的键值对并返回zhangsan的键值', d3.pop('zhangsan'))
print('---', d3)

print('12.删除字典d3最后一对键值对并返回剩余键值对', d3.popitem())
print('---', d3)


my_list = []

for i in range(3):
    my_dict = {} #每循环创建一个字典
    name = input('请输入姓名')
    age = input('请输入年龄')
    my_dict['name'] = name
    my_dict['age'] = age
    my_list.append(my_dict)

#遍历列表，列表中存在的都是字典，所2.7 dict{}字典.py有item 是字典
for item in my_list: #item 是字典
    print(item['name'], item['age']) #根据字典的key获取value

name_list = [] #定义学生信息表

i = 0   #书写循环获取信息
while i < 3:
    name = input('请输入姓名')
    age = input('请输入年龄')
    my_dict1 = {'name':name, 'age':age} #将name和age存入列表
    name_list.append(my_dict1) #将学生信息存入列表
    print('保存成功')
    i += 1

for item in name_list:
    print(item['name'],item['age'])