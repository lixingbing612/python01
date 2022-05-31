class Students():
    name = "张三"
    grade = "2"


#一.类变量  直接定义在类内，调用时可以直接使用类名或者实例对象   作用范围最大
# 1.通过类名调用      类名.变量名
print(Students.name)
print(Students.grade)

# 2.通过实例化进行调用       对象名.变量名
s = Students()
print(s.name)
print(s.grade)

#
print('-'*20)
#二.实例变量     一般情况下定义的方法内部，使用self.变量名 = value ，调用时直接使用实例对象
class Students():
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        print('{}年级的学生{}正在学习'.format(self.grade, self.name))


s = Students("张三", 5)  #对象名.方法()


class Students():
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def eat(self):
        print(self.name,'是',self.grade,'正在吃饭')

s = Students("张三", '5年级')
print(s.eat())      #对象名.方法()
#
print('='*20)
#三.局部变量     定义在方法内部， 变量名 = value ， 调用时只能在该方法的内部使用
class Students():
    def study(self,name):
        say = "hello"
        print("{} {}".format(say,name))
s = Students()
s.study("张三")