password = 'a123456'
i = 3 # 剩余机会
while i > 0:
	pwd = input('请输入密码： ')
	if pwd == password:
		print('登入成功！')
		break #逃出循环
	else:
		i = i-1
		print('密码错误！还有',i, '次机会')