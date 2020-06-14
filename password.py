password = 'a123456'
i = 3 # 剩余机会
while i > 0:
	i = i-1
	pwd = input('请输入密码： ')
	if pwd == password:
		print('登入成功！')
		break #逃出循环
	else:
		print('密码错误！')
		if i > 0:
			print('还有', i, '次机会')
		else:
			print('没机会尝试了！要锁账号了啦')