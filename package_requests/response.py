

"""请求方法的返回值response为 Response 对象，我们可以从这个对象中获取所有我们想要的响应信息。
response.status_code 状态码
response.url 请求url
response.encoding 查看/修改响应头部字符编码
response.text 文本形式的响应内容
response.json() JSON形式的响应内容
response.headers 获取响应头

案例
1. 访问百度首页的接口 http://www.baidu.com ，获取以下响应数据
2. 获取响应状态码
3. 获取请求URL
4. 获取响应字符编码
5. 获取响应头数据
6. 获取文本形式的响应内容"""

import requests

response = requests.get("http://www.baidu.com")

response.encoding = 'utf-8'	# 修改字符编码
print("获取状态码",response.status_code)
print("请求url",response.url)
print("获取字符编码",response.encoding)
print("获取文本形式",response.text)
# print("JSON形式的响应内容",response.json())
print("获取响应头",response.headers)
print("获取消息",response.reason)

