
# 存在的问题 ：
"""
1. 无法查看运行的用例数，比如成功几条，失败几条
2.如果失败 是什么导致的？最好给除失败的错误日志
3.无法去组织用例，不能控制哪些用例执行，哪些不执行
"""

# 解决方案 ： 使用unittest解决问题 测试框架 对用例分类套件 如 冒烟测试 回归测试

"""
unittest框架的功能： 
	1.unittest.TestCase()
	能对测试用例进行测试（断言）
	测试的结果能看到，及失败的原因
	可以进行初始化和清除功能
所编写的测试用例必须是一个类，且必须继承TestCase类
每个测试方法都必须是test开头
编写测试类建议Test开头
编写的模块建议小写test开头
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
	unittest.main()
