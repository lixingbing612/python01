# 类的定义
'''
class 类名：
    类属性
    类方法
'''


# 实例: 创建学生类，要求有属性：姓名和年级 ; 函数有：学习的方法，打印学生的上课情况


class Students():
    name = ' '
    grade = ' '
    status = ' '

    def study(self):
        print('{}年级的学生{}正在{}'.format(self.grade, self.name, self.status))



s1 = Students()
print(s1)
s1.name = '张狗蛋'
s1.grade = '2'
s1.status = '玩手机'
print(s1.study())

s2 = Students()
print(s2)
s2.name = '李铁柱'
s2.grade = '3'
s2.status = '调戏女同学'
print(s2.study())
