

# 测试用例过多导致代码冗余，维护性不高 ， 主要原因： 代码重复，数据不同

# 解决方案 ： 使用 parameterized 实现数据参数化，将列表中的数据在一条测试用例中循环运行，起到多条数据测试的作用

# 具体方法 ： expand(list) , list : 数据列表		注意 ： 使用了expand() ，需要把它放在测试方法前 加 @ ，这个叫装饰器

# 前置条件 ： 下载安装： pip install parameterized

# 1. 导入包
from parameterized import parameterized
import unittest
from project02.iter03_add_user import login

# 测试数据

lst_data = [(0,'admin','123456'),
			(0,'dev','123456'),
			(1,'dev','1234567'),
			(1,'uyiuoiy','123456'),
			(1,'','123456'),
			(1,'admin','')]

class Testlogin(unittest.TestCase):


	@parameterized.expand(lst_data)
	def test_login(self,except_value,username,password):	# test_login()内对应lst内的值 读取@parameterized.expand的lst_data

		actual_value = login(username,password).get('code')
		self.assertEqual(except_value,actual_value)


if __name__ == '__main__':
    unittest.main()