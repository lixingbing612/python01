

# loguru模块
# 作用 ：通过记录日志排查问题

"""
功能
1. 可以格式化日志
2. 着色
3.生成到文件
4.显示不同的日志级别
5.只使用一个对象
"""

# 1.下载安装 ：pip install loguru

# 2.导包：
from loguru import logger # 导入loguru的logger对象

# 3.打印一条日志 ：hello word
logger.info("hello word")  # 打印的为日志格式化

# 4.输出不同日志级别
# debug :调试日志
# info :普通日志
# warning :警告日志
# success ：成功日志
# error :错误日志
logger.debug("这是一条debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")

# 5.输出到文件 ：add()
# add(filename,format,level) 文件名，输出格式：{}，级别
logger.add("file.log", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module} | {line}| {message}",level="INFO")
logger.debug("这是一条debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")
logger.debug('日志第二天')
# 文件的日志只有在level级别及以上才会输出

# 6.格式化字符串
logger.info("他的的外号叫{}，他的名字是{name}","帅锅",name="张三")

# 7，文件保存
# logger.add("file_1.log", rotation="500 MB") # 文件过大就会重新生成一个文件
# logger.add("file_2.log", rotation="12:00") # 每天12点创建新文件
# logger.add("file_3.log", rotation="1 week") # 文件时间过长就会创建新文件
# logger.add("file_X.log", retention="10 days") # 一段时间后会清空
# logger.add("file_Y.log", compression="zip") # 保存zip格式
