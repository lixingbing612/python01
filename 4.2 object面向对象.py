# 面向对象：是一种编程思想，把现实生活中的事物抽象定义成具体的类，在类中申明属性和方法，再去初始化对象
#使用函数实现调用对象
def start():
    print('启动')


def run():
    print('运行')


def stop():
    print('停止')


start()
run()
stop()

print('=' * 20)

#使用类方法调用对象
#1.定义一个类：class
class Elevator:
#2.在类里面声明属性（数据）和方法（函数）
    button = '开/关'
    floor = 15
    prple_nums = 13

    def start(self):
        print('打开电梯')

    def stop(self):
        print('关闭电梯')

    def run(self):
        print('电梯运行')

# 3.定义一个具体的对象，叫初始化对象：对象名=类名（）
e = Elevator()
# 4.使用对象调用方法或属性：对象名.方法||对象名.属性
e.start()
e.stop()
e.run()


a = 1
print('a:', id(a))
b = a
print('b:', id(b))

a = 10
print('a:', id(a))
print('b:', id(b))