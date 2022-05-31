# main属性：__main__		运行入口  python脚本被作为模块(module)引入(import)时，其中的main()函数将不会被执行
# main
"""
def add(x,y):
    a = x + y
    return a

def sub(x,y):
    b = x - y
    return b

if __name__ == '__main__':   		#main的运行入口，不影响main之后的代码运行
    print(__name__)
    print(add(3,5))
    print(sub(4,3))
"""
import main1
print(main1.add(9,24))		#这里只调用main1中main前面的代码，不会输出main后面的结果
print(__name__) 			#这里的name