# main属性：__main__		运行入口  python脚本被作为模块(module)引入(import)时，其中的main()函数将不会被执行

def add(x,y):
    a = x + y
    return a

def sub(x,y):
    b = x - y
    return b

print(add(1,1))

if __name__ == '__main__':   		#main的运行入口，不影响main的代码运行
    print(add(3,5))
    print(sub(4,3))