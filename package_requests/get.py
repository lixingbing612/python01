
# 请求百度地址 http://www.baidu.com

# 1. 导包
import requests

# 2. 使用get方法请求
response = requests.get('http://www.baidu.com')
# 获取响应内容
print(response.text)	# text 获取网站的文本信息
