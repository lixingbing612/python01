
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

	2.unittest.TestSuite()
	将不同的测试用例添加到不同的套件中
	a.可以添加不同的测试用例到套件中（单条）
	b.可以添加不同的测试用例组到套件中（一组）

	3.unittest.TestLoder()
	可以将测试套件进行运行

	4.unittest.TextTestRunner()
	可以进行批量运行测试用例
"""
