
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

print("-"*300)

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

print("-"*300)

#定义一个函数func功能如下
my_list = [{'id': 1, 'money': 10}, {'id': 2, 'money': 20},
           {'id': 3, 'money': 30}, {'id': 4, 'money': 40}]

def func():

    for i in my_list: #i变量，字典类型
    #1.如果字典id奇数则对money加20
        if i.get('id') % 2 == 1:
            i['money'] = i.get('money') + 20
    #2.如果字典id偶数则money加10
        else:
            i['money'] = i.get('money') + 10
    #打印输出列表
    print(my_list)

func()


user_dict = {"登录":[{'role': 'admin', 'account': 'admin', 'password': '123456', 'dept': 'tester'},{'role': 'user', 'account': 'dev', 'password': '123456', 'dept': 'dev'}],
             "注册":[{'account': 'admin', 'password': '123456'},{ 'account': 'dev', 'password': '123456'}]}
user_list = []

opt = input('请输入查询登录/注册数据')
if opt == '登录':
    print('获取登录数据：')
    for x in user_dict.get('登录'):
        i = (x.get("role"),x.get("account"),x.get("password"),x.get("dept"))
        user_list.append(x)
elif opt == '注册':
    print('获取注册数据：')
    for x in user_dict.get('注册'):
        i = (x.get("account"),x.get("password"))
        user_list.append(x)
    else:
        print('输入错误')
print(user_list)

