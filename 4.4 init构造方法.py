# class的构造方法：每次调用类的时候会自动被调用 ，主要用来初始化数据
'''
语法格式：
def __init__(self,...):
    代码块
'''


class Students:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        print('此方法会被自动执行')

    def study(self):
        print('{}年级的学生{}正在学习'.format(self.grade, self.name))


s1 = Students('张三', 6)
s1.study()

class Student:
	def __init__(self, name, grade, hobby):
		self.name = name
		self.grade = grade
		self.hobby = hobby

	def study(self):
		print('学生{},在读{}年级,喜欢{}'.format(self.name, self.grade, self.hobby))


s = Student('大牛', '6', '扣篮')
s.study()