"""需求：
1. 访问TPshop搜索商品的接口，通过查询字符串的方式传递搜索的关键字 iPhone ，并查看响 应数
据
2. 请求路径格式为： http://localhost/Home/Goods/search.html?q=iPhone
实现分析：
请求方式：GET
请求路径： http://localhost/Home/Goods/search.html
传参方式：查询字符串（q=iPhone）
示例代码："""

import requests

# response = requests.get("http://localhost/Home/Goods/search.html?q=iPhone")
# print(response.text)


# url = "http://localhost/Home/Goods/search.html?q=iPhone"
# response = requests.get(url)
# print(response.text)


# url1 = "http://localhost/Home/Goods/search.html"
# params = {"q":"iPhone"}
# response = requests.get(url1,params=params)
# print(response.text)


url2 = "http://localhost/Home/Goods/search.html"
params = "q=iPhone"
response = requests.get(url2,params=params)
print(response.text)