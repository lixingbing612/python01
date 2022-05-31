#使用try...except语句处理异常
'''
语法格式
try:
	代码块
except Exception as e:		#Exception是最大的异常范围，可细分详细的异常
	处理异常代码块
'''

def div(x,y):
	z = x / y
	return z
# print(div(2,0))	#异常，2不能除于0

def div1(x,y):
	try:
		z = x / y
		return z
	except Exception as e:
		print('除法出现被0除的情况')

print(div1(3,0))

print('-'*20)
def div3(x,y):
	try:
		z = x / y
	except ZeroDivisionError as e:
		print(e)

print(div3(2,0))

print('-'*20)

# 使用try...except...finally语句处理异常
'''
语法格式
try:
	代码块
except Exception as e:
	处理异常代码块
finally:
	必须执行的代码块	
'''

try:
	f = open('a.txt','r')
	lines = f.readlines()
	print(2/0)

	for x in lines:
		print(x)
except Exception as e:
	print(e)

finally:
	print('跳过异常执行下面的代码')
	f.close()