#多肽
#1.必须是继承关系
#2.必须是子类的方法复写了父类的方法
"""
面向对象的多肽 父类有相同的方法时，子类可重新定义方法使用会优先调用子类方法，也可 super().方法(属性) 调用父类方法
继承和多肽的区别：
继承：子类直接调用父类方法
多肽：子类的方法直接覆盖了父类的方法
"""


class People():


    def eat(self, people_type):
        print(people_type, '在吃饭')


class Student(People):
    def eat(self, grade):
        super().eat(grade)  #把父类的已有方法进行继承调用
        print(grade,'年级学生在吃饭')  #这个是对功能的扩展


class Teacher(People):
    def eat(self, subject,time):
        print('{}的老师在{}时吃饭'.format(subject,time))


s = Student()
s.eat('1')  #有相同方法时调用了父类方法


s = Teacher()
s.eat('English','12:00') #先调用了子类的方法
