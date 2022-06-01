

# 测试用例过多导致代码冗余，维护性不高 ， 主要原因： 代码重复，数据不同

# 解决方案 ： 使用 parameterized 实现数据参数化，将列表中的数据在一条测试用例中循环运行，起到多条数据测试的作用

# 具体方法 ： expand(list) , list : 数据列表		注意 ： 使用了expand() ，需要把它放在测试方法前 加 @ ，这个叫装饰器

# 前置条件 ： 下载安装： pip install parameterized

# 1. 导入包
# from parameterized import parameterized # 导入参数化包的参数化方法
# import unittest
# from project02.iter03_add_user import login
#
# # 测试数据
#
# lst_data = [(0,'admin','123456'),		# 定义测试数据在列表中
# 			(0,'dev','123456'),
# 			(1,'dev','1234567'),
# 			(1,'uyiuoiy','123456'),
# 			(1,'','123456'),
# 			(1,'admin','')]

# class Testlogin(unittest.TestCase):		#创建测试登录的类 调用unittest的TestCase方法
#
#
# 	@parameterized.expand(lst_data)		# 使用@parameterized.expand装饰器可以为测试函数的参数进行参数化
# 	def test_login(self,except_value,username,password):	# test_login()内对应lst内的值 self,code预期结果，输入的数据
#
# 		actual_value = login(username,password).get('code')		# 实际结果 = 登录的输入值来get到code
# 		self.assertEqual(except_value,actual_value)			# self.断言判断预期结果和实际结果是否相等
#
#
# if __name__ == '__main__':
#     unittest.main()


from project02.iter03_add_user import login
from parameterized import parameterized
import unittest

lst = [(0,'admin','123456'),
			(0,'dev','123456'),
			(1,'dev','1234567'),
			(1,'uyiuoiy','123456'),
			(1,'','123456'),
			(1,'admin','')]

class Testlogin(unittest.TestCase):


	@parameterized.expand(lst)
	def testlogin(self,except_value,username,password):

		actual_vauel = login(username,password).get('code')
		self.assertEqual(except_value,actual_vauel)

if __name__ == '__main__':
    unittest.main()




