

'''
TestSuite()功能
addTest(testcase)	,testcase代表的是测试用例	可以添加不同的测试用例到套件中（单条）
addTests(tests)		,tests代表的是测试用例组		可以添加不同的测试用例组到套件中（一组）
'''
""" 
	2.unittest.TestSuite()
	将不同的测试用例添加到不同的套件中
	a.可以添加不同的测试用例到套件中（单条）
	b.可以添加不同的测试用例组到套件中（一组）
	# 2.使用TextTestRunner()类进行运行测试套件

run(suite)	,suite就是测试套件，可以将测试套件可以进行运行	
解决了按照不同测试套件去运行

"""
from project02.iter03_add_user import login		# 导入project02.iter03_add_user的方法login
import unittest		# 导入unittest类
import sys	# 导入sys包

class Testlogin(unittest.TestCase):
	# 定义初始化类，初始化方法，清空类，清空方法
	@classmethod
	def setUpClass(cls) -> None:
		print('开始运行方法：',sys._getframe().f_code.co_name)	# sys._getframe().f_code.co_name调用sys模块的函数

	def setUp(self) -> None:
		print('开始运行方法：',sys._getframe().f_code.co_name)	# sys._getframe().f_code.co_name调用sys模块的函数

	@classmethod
	def tearDownClass(cls) -> None:
		print('开始运行方法：',sys._getframe().f_code.co_name)	# sys._getframe().f_code.co_name调用sys模块的函数

	def tearDown(self) -> None:
		print('开始运行方法：',sys._getframe().f_code.co_name)	# sys._getframe().f_code.co_name调用sys模块的函数

	# 1.测试登录的测试用例
	# case1 ：输入正确用户名和密码
	def test_login_success(self):	# 定义登录成功
		print('开始运行方法：',sys._getframe().f_code.co_name)
		except_value = 0		# 预期结果code = 0
		actual_value = login('admin','123456').get('code')		# 实际登录账号admin密码123456后获得的code
		self.assertEqual(except_value,actual_value)				# self断言预期结果和实际结果是否相等
	# case2 ：输入错误的用户名或密码
	def test_login_wrong(self):		# 定义错误用户或密码登录
		print('开始运行方法：',sys._getframe().f_code.co_name)
		except_value = 1		# 预期结果code = 1
		actual_value = login('admin','12345').get('code')		# 实际登录账户对密码错获得的code
		self.assertEqual(except_value,actual_value)				# self断言预期结果和实际结果是否相等
	# case3 ： 输入空的用户名或密码
	def test_password_null(self):	# 定义账号或密码空登录
		print('开始运行方法：',sys._getframe().f_code.co_name)
		except_value = 1		# 预期code = 1
		actual_value = login('','123456').get('code')			# 实际登录账户空密码正确活动code
		self.assertEqual(except_value,actual_value)				# self断言预期结果和实际结果是否相等

if __name__ == '__main__':
	# unittest.main() # 这个是运行当个测试用例
	suite_a = unittest.TestSuite()		# 创建suite_a为调用unitestSuite的方法
	suite_a.addTest(Testlogin('test_login_success'))	# 在套件suite_a里面添加test_login_success的测试用例
	suite_a.addTest(Testlogin('test_login_wrong'))		# 在套件suite_a里面添加test_login_wrong的测试用例
	suite_a.addTest(Testlogin('test_password_null'))	# 在套件suite_a里面添加test_password_null的测试用例
	print(suite_a)

	runner = unittest.TextTestRunner()		# 创建运行器runner调用unnitest.TextTestRunner的方法
	runner.run(suite_a)			# runner运行套件suite_a


