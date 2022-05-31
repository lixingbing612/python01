def login():
	name=input('请输入账号：')
	pwd=input('请输入密码：')
	list=[{'role':'admin','account':'admin','password':'123456','dept':'admin'},{'role':'user','account':'user','password':'123456','dept':'test'}]

	i = 0
	while i <len(list):
		if name == list[i]['account'] and pwd == list[i]['password']:
			d1={'code': 0, 'message': '登录成功', 'list': list[i]}
			print(d1)
		elif name == list[i+1]['account'] and pwd == list[i+1]['password']:
			d2={'code': 0, 'message': '登录成功', 'list': list[i+1]}
			print(d2)
		elif name == '' or pwd == '':
			d3={'code': 1, 'message': '账户或密码不能为空，请重试'}
			print(d3)
			login()
		else:
			d4={'code': 1, 'message': '账户或密码错误，请重试'}
			print(d4)
			login()
		break

login()


