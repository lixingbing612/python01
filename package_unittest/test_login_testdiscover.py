


# 3.使用的是TestLoader()		可以批量去添加测试用例，解决单条测试用例效率的问题
"""
unittest.TestLoder()
	可以批量运行测试用例 ： discover(test_dir,patten='test*.py')  test开头	.py结尾
	test_dir : 指定要搜索的路径
	patten : 指定匹配的模式 , 在test_dir目录下搜索所有patten的文件

"""

# 2.使用TextTestRunner()类进行运行测试套件
'''
run(suite)	,suite就是测试套件，可以将测试套件可以进行运行	
解决了按照不同测试套件去运行
'''

from project02.iter03_add_user import login		# 导入project02.iter03_add_user的方法login
import unittest		# 导入unittest类
import sys	#导入sys包


class TestLogin(unittest.TestCase):		# Testlogin继承unittest.TestCase类

	# 初始化类方法		setUpclass()	整个类在运行前，先运行setupClass()，只运行一次
	@classmethod
	def setUpClass(cls) -> None:
		print('开始运行方法：',sys._getframe().f_code.co_name)	# sys._getframe().f_code.co_name调用sys模块的函数

	# 清空类方法		tearDownclass()	整个类在运行结束时，先运行tearDownClass()，只运行一次
	@classmethod
	def tearDownClass(cls) -> None:
		print('开始运行方法：',sys._getframe().f_code.co_name)	# sys._getframe().f_code.co_name调用sys模块的函数

	# 初始化方法 ： setUp()			如果每次运行测试方法前都需要先执行setup()
	def setUp(self) -> None:
		print('开始运行方法：',sys._getframe().f_code.co_name)	# sys._getframe().f_code.co_name调用sys模块的函数

	# 清空方法 ： tearDown()			如果每次运行测试方法后都需要先执行tearDown()
	def tearDown(self) -> None:
		print('开始运行方法：',sys._getframe().f_code.co_name)	# sys._getframe().f_code.co_name调用sys模块的函数

	# 1.测试登录的测试用例

	# case1 ：输入正确用户名和密码
	def test_login_success(self):
		print('开始运行方法：',sys._getframe().f_code.co_name)
		except_value = 0 	# 预期结果是0
		actual_value = login('admin','123456').get('code')	# 实际结果 需导入登录方法 alt+enter，调用project02.iter03_add_user的login模块
		self.assertEqual(except_value,actual_value)	# self调用unittest_TestCase的方法，断言期望值是不是和实际值相等，如果相等会输出结果

	# case2 ：输入错误的用户名或密码
	def test_user_wrong(self):
		print('开始运行方法：',sys._getframe().f_code.co_name)
		except_value = 1 	# 预期结果是1
		actual_value = login('aaaaa','123456').get('code')	# 实际结果 需导入登录方法 alt+enter，调用project02.iter03_add_user的login模块
		self.assertEqual(except_value,actual_value)	# self调用unittest_TestCase的方法，断言期望值是不是和实际值相等，如果相等会输出结果

	# case3 ： 输入空的用户名或密码
	def test_password_is_null(self):
		print('开始运行方法：',sys._getframe().f_code.co_name)
		except_value = 1 	# 预期结果是1
		actual_value = login('admin',' ').get('code')	# 实际结果与预期结果不符合，输出结果，调用project02.iter03_add_user的login模块
		self.assertEqual(except_value,actual_value)	# self调用unittest_TestCase的方法，断言期望值是不是和实际值相等，如果相等会输出结果

if __name__ == '__main__':

	# 创建一个套件a
	suite_a = unittest.TestLoader().discover('.',pattern='test_login_testdiscover.py')		# 调用unittest的TestLoader()的方法discover()在当前目录.搜索test_login_testdiscover.py文件
	print(suite_a)

	# 运行套件suite_a
	runner = unittest.TextTestRunner()  # 创建运行器
	runner.run(suite_a)	# runner调用run()方法
