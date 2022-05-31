'''# 需求-迭代1：登录功能
# 1. 定义两条用户数据 ，要求用户数据的属性包括用户角色，用户账号，密码，部门
# 2. 要求返回的格式是字典形式 ，包含两个字段，code和message ,code为0代表成功，为1代表失败 ；message给出相应的提示 ，格式如 ：{'code':0,'message':'登录成功'}
# 3. 用户通过控制台输入用户名和密码，判断用户名和密码是否和定义数据中的用户名密码相匹配，若匹配返回成功登录消息体，并把用户列表也追加到返回结果中,{'code':0,'message':'登录成功',user_list:[]}
# 4. 若用户名输入为空或密码输入为空，都给出对应的提示，如用户名不能为空
# 5. 若用户名或密码不匹配，都给出登录失败，请检查您的用户名或密码是否填写正确提示


# 1.定义用户默认数据 [a1,a2]=[{},{}]
user_list = [{'role': 'admin', 'account': 'admin', 'password': '123456', 'dept': 'tester'},
			 {'role': 'user', 'account': 'dev', 'password': '123456', 'dept': 'dev'}]

# 2.定义默认返回结果
result = {'code': '', 'message': ''}


# 3.定义登录功能
def login(username, password):
	# 用户名或密码为空的情况
	if username == None or username == '':
		result.update({'code': '1', 'message': '用户名或密码不可为空'})
		return result
	if password == None or password == '':
		result.update({'code': '1', 'message': '用户名或密码不可为空'})
		return result
	# 登录成功的情况
	for userinfo in user_list:
		if username == userinfo.get('account') and password == userinfo.get('password'):
			result.update({'code': '0', 'message': '登录成功', 'user_list': user_list})
			return result

	# 用户名或密码不匹配或错误的情况
	result.update({'code': '1', 'message': '用户名或密码不正确，请重新输入'})
	return result


if __name__ == '__main__':
	username = input('请输入用户名')
	password = input('请输入密码')
	print(login(username, password))

'''

# # 1.定义用户默认数据 [a1,a2]=[{},{}]
# user_list = [{'role': 'admin', 'account': 'admin', 'password': '123456', 'dept': 'tester'},
# 			 {'role': 'user', 'account': 'dev', 'password': '123456', 'dept': 'dev'}]
#
# # 2.定义默认返回结果
# result = {'code':'','message':''}
#
# # 3.定义登录功能
# def login (username,password):
#
# 	# 用户名或密码为空的情况
# 	if username is None or username == '':
# 		result.update({'code': '1', 'message': '不可为空'})
# 		return result
# 	if password is None or password == '':
# 		result.update({'code': '1', 'message': '不可为空'})
# 		return result
# 	# 登录成功的情况
# 	for userinfo in user_list:
# 		if username == userinfo.get('account') and password == userinfo.get('password'):
# 			result.update({'code': '0', 'message': '登录成功'})
# 			return result
# 	# 用户名或密码不匹配或错误的情况
# 	result.update({'code': '1', 'message': '用户名或密码错误'})
# 	return result
# if __name__ == '__main__':
#     username = input('请输入用户名')
#     password = input('请输入密码')
#
# print(login(username,password))




#定义用户数据
user_list = [{'role': 'admin', 'account': 'admin', 'password': '123456', 'dept': 'tester'},
			 {'role': 'user', 'account': 'dev', 'password': '123456', 'dept': 'dev'}]
#定义返回结果
result = {'code':'','message':''}
#定义登录功能
def login(username,password):
	#当用户名或密码为空时
	if username is None or username == ' ':
		result.update({'code':'1','message':'用户名不可为空'})
		return result
	if password is None or username == ' ':
		result.update({'code':'1','message':'密码不可为空'})
		return result
	#登录成功时
	for userinfo in user_list:
		if username == userinfo.get('account') and password == userinfo.get('password'):
			result.update({'code':'0','message':'登录成功'})
			return result
	#登录失败
	result.update({'code':'1','message':'用户名或密码错误'})
	return result

# #4.用户查询功能
# 定义查询功能
def get_user(username):
	pass

if __name__ == '__main__':

# 	#1.进行循环以便用户做各种操作
	flag = True
	while flag:
# 提供用户的各种选择，1.登录操作，2.查询操作，q.退出操作
		vls = input('1.登录操作，2.查询操作，q.退出操作')
# 		#当输入其他符号时进行重新输入
		if not vls in ('1','2','3','q','quit'):
			print('-'*200)
			continue
# 		#进行登录操作
		if vls == '1':
			username = input('请输入用户名')
			password = input('请输入密码')
			login_result = login(username,password)
			print(login_result)
			print('-'*200)
			continue
# 		#进行查询功能
		if vls == '2':
			username = input('查询的用户')
			get_result = get_user()
			print(get_result)
			continue
# 		#退出
		if vls in ('q','quit'):
			flag = False
			print('退出成功')

