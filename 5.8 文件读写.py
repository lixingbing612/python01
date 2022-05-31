#文件读写
#1.读取文件
"""
1.打开文件 文件名.模式
2.读取文件
3.关闭文件
"""
#读取所有内容
a = open('a.txt', 'r')
look = a.read()
print(look)
a.close()
'''
打开文件
循环对
赋值
打印
如果没有
打断
'''
print("-"*20)
#按行读取内容（readline）
a = open('a.txt', 'r')
while True:
    look = a.readline()
    print(look) #括号内可加end=''
    if not look:
        break
a.close()
"""
读取文件
赋值在读取所有行中
打印赋值
"""
print("-"*20)
#读取所有行（readlines）
a = open("a.txt", "r")
for x in a.readlines():
    print(x)


#2。写入文件w/a
"""
1.打开文件
2.写入文件
3.关闭文件
"""
a = open("a.txt", "a")
pen = a.write("pleas do not look me")
a.close()