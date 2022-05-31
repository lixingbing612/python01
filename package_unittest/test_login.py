
from project02.iter03_add_user import login
from loguru import logger
# 1.测试登录的测试用例

# case1 ：输入正确用户名和密码

# case2 ：输入错误的用户名或密码

# case3 ： 输入空的用户名或密码


# 2.进行测试 - 使用断言 assert 值1 操作符 值2
# 测试方式 ： 预期结果 和 实际结果 进行比较

# 以上用例 登录成功的预期结果是code = 0 ，

login_result = login('admin','123456')
logger.debug('登录返回数据：{}'.format(login_result))
assert 0 == login_result.get('code')
# assert 1 == login_result.get('code')

# 存在的问题 ：
"""
1. 无法查看运行的用例数，比如成功几条，失败几条
2.如果失败 是什么导致的？最好给除失败的错误日志
3.无法去组织用例，不能控制哪些用例执行，哪些不执行
"""
