import random
x = input('please enter min number: ')
x = int(x)
y = input('please enter max number: ')
y = int(y)
r = random.randint(x, y)
count = 0
while True:
	count += 1
	num = input('Guess the number: ')
	num = int(num)
	if num == r:
		print('you are right!')
		if count == 1:
			print('you guessed', count, 'time')
		elif count > 1:
			print('you guessed', count, 'times')	
		break
	else:
		if num > y:
			print(x, '~', y)
		elif num < x:
			print(x, '~', y)
		elif num > r:
			y = num
			print (x, '~', y)
		elif num < r:
			x = num
			print (x, '~', y)

