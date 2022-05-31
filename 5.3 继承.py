# 继承
#1.两个类之间存在父子关系，在子类中直接写父类的类名即可继承，比如：Student(people)
#2.只要产生了继承关系，那么子类就可以直接调用父类的方法或属性
class People:

	age = 0
	__height = 180

	def eat(self,people_type):
		print(people_type,'在吃饭')

class Student(People):

	pass

class Teacher(People):

	pass

a = Student()
a.eat('学生')	#继承父类people的方法
Student.age = 20	#可直接设置子类的属性值
print(Student.age)

b = Teacher()
b.eat('老师')
Teacher.age = 30
print(Teacher.age)
# print(Teacher.__height) #父类封装的属性不可调用