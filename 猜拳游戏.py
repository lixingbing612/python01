#猜拳游戏
import random  # 导入随机数包
num = random.randint(1,3)

player = int(input('请出拳石头（1），剪刀（2），布（3）：'))
computer = random.randint(1,3)
if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
	print('恭喜你获得胜利')
elif player == computer:
	print('平局')
else:
	print('你输了，再来一局')


num = random.randint(1,10)

while True:
	my_num = int(input('输入1-10之间整数'))
	if my_num == num:
		print('恭喜猜对，数字是%d'%num)
		break
	elif my_num > num:
		print('太大了')
	else:
		print('太小了')