# 需求-迭代2：用户查询功能:
# 1. 用户查询功能必须是在登录以后才能调用 ，否则给出权限不足提示
# 2. 若输入的用户名正确，返回登录用户的信息，password字段不显示  。
# 3. 若输入的用户名不正确 ，给出无查询结果的提示
# 4. 查询支持模糊查询。

#1.定义用户默认数据 [a1,a2]=[{},{}]
user_list = [{'role':'admin','account':'admin','password':'123456','dept':'tester'},{'role':'user','account':'dev','password':'123456','dept':'dev'}]

#2.定义默认返回结果
result = {'code':0,'message':''}

#3.定义登录功能
def login(username,password):


	# 用户名或密码为空的情况
	if username is None or	username == '':
		result.update({'code': 1,'message': '用户名不能为空'})
		return result
	if password is None or password == '':
		result.update({'code': 1,'message': '密码不能为空'})
		return result

	# 登录成功的情况
	for userinfo in user_list:
		if username == userinfo.get('account') and password == userinfo.get('password'):
			result.update({'code': 0,'message':'登录成功！','user_list':user_list})
			return result


	# 用户名或密码不匹配或错误的情况
	result.update({'code': 1,'message':'请检查您的用户名或密码是否填写正确'})
	return result


#4.用户查询功能
def get_user(username):

# 判断用户是否登录，登录才可查询 ，否则给出权限不足提示  code!=0代表未登录
	if not result.get('code'):  #默认为0 改not
		result.update({'code':11,'message':'用户未登录，无法查询'})
		return result

# 输入正确用户名进行查询，返回结果不展示password（支持模糊查询）
	result.update({'user_list':[]})		#登录成功的情况下更新用户列表
	lst = [] #存放查询到的结果的数据
	for x in user_list:			#循环x在用户列表
		account = x.get('account')	#获取x列表的account赋值account
		if username in account:		#支持模糊查询 如果=代表精确查询
			x.pop('password')		#删掉password的字段
			lst.append(x)

	#判断列表里的数据，如果列表不为空，代表查询成功，返回对应结果
	if lst:
		result.update({'message':'查询用户成功！','user_list':lst})  #更新lst列表为新的结果
		return result

# 若输入的用户名不正确，返回无查询结果
	result.update({'code': 12,'message':'未查到用户名，请重新输入'})
	return result

if __name__ == '__main__':

	#1.进行循环以便用户做各种操作
	flag = True

	while flag:	#条件为真

		#提供用户的各种选择，1.登录操作，2.查询操作，q.退出操作
		vls = input('如需操作请输入编号'
					'\n 1.进行登录'
					'\n 2.查询用户，请输入用户名'
					'\n q.退出'
					'\n 请输入操作编号：')

		#当输入其他符号时进行重新输入
		if not vls in ('1','2','q','quit'):  # not
			print('-'*200)
			continue

		#进行登录操作
		if vls == '1':
			username = input('请输入用户名:')
			password = input('请输入密码:')
			login_result = login(username,password)
			print(login_result)
			print('-'*200)
			continue

		#进行查询功能
		if vls == '2':
			name = input('请输入要查询的用户名:')
			get_result = get_user(name)
			print(get_result)
			print('-'*200)
			continue

		#退出
		if vls in ('q','quit'):
			flag = False
			print('退出成功!')
