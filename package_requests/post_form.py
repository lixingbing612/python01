
# post 请求表单类型
# response = requests.get(url, data=None, json=None)	url : http协议的url		data/json : 请求体的数据
"""
:param url: 请求的URL
:param data: (可选) 要发送到请求体中的字典、元组、字节或文件对象
:param json: (可选) 要发送到请求体中的JSON数据
:rtype: requests.Response

需求：
1. 请求TPshop项目的登录接口，请求数据（username: 13112345678, password: 123456,
verify_code: 1234）
2. 登录接口URL：http://localhost/index.php?m=Home&c=User&a=do_login
"""

# 1. 导包
import requests

# 2. 使用post方法请求
login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data = {"username": "13112345678", "password": "123456","verify_code": "1234"}
response = requests.post(login_url,data=login_data)

print(response.text)
