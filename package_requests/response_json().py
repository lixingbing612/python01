

# 1. 导包
import requests

# 2. 使用post方法请求 发送POST请求
login_url = "http://121.196.13.152:8080/admin/auth/login"
login_data = {"username": "admin123", "password": "admin123"}
headers = {"Content-Type":"application/json"}
response = requests.post(login_url, json=login_data, headers = headers)

# 获取响应内容
text_result = response.text
json_result = response.json()

print("text打印为文本字符串",text_result)
print("json()打印为字典",json_result)

print(json_result.get("data").get("adminInfo"))
