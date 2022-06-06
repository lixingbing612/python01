
# post 请求json类型
# response = requests.get(url, data=None, json=None)	url : http协议的url		data/json : 请求体的数据
"""
:param url: 请求的URL
:param data: (可选) 要发送到请求体中的字典、元组、字节或文件对象
:param json: (可选) 要发送到请求体中的JSON数据
:rtype: requests.Response

需求：
1. 请求微商城项目的登录接口，请求数据（ {"username":"admin123","password":"admin123"}）
2. 登录接口URL：http://121.196.13.152:8080/admin/auth/login
"""

# 1. 导包
import requests

# 2. 使用post方法请求 发送POST请求
login_url = "http://121.196.13.152:8080/admin/auth/login"
login_data = {"username": "admin123", "password": "admin123"}
response = requests.post(login_url, json=login_data)
# 获取响应内容
print(response.text)

