import random
count1 = 0
count2 = 0
count3 = 0
i = 0
# 1. fix i is not changing
# 2. keep i between 0 to size of letters - 1.
def func():
	global count1, count2, count3, i

	letters = ('rock','paper', 'scissor')
	
	player1 = letters[i]
	
	print('player 1 has selected ', player1)
	player2 = random.choice(letters)
	# print('player 2 has selected ', player2)


	if player1 == 'rock' and player2 == 'paper':
		print('player 2 has won')
		
		count2 = count2 + 1
		i = i + 1
		player1 = letters[i]
	elif player1 == 'rock' and player2 == 'scissor':
		# print('player 2 has won')
		count1 = count1 + 1
	elif player1 == 'paper' and player2 == 'rock':
		# print('player 2 has won')
		count1 = count1 + 1
	elif player1 == 'paper' and player2 == 'scissor':
		print('player 2 has won')
		
		count2 = count2 + 1
		i = i + 1
		player1 = letters[i]
	elif player1 == 'scissor' and player2 == 'paper':
		# print('player 2 has won ')
		count1 = count1 + 1
	elif player1 == 'scissor' and player2 == 'rock':
		print('player 2 has won')
		
		count2 = count2 + 1
		i = 0
		player1 = letters[i]
	elif player1 == player2:
		# print('Try again')
		count3 = count3 + 1
	else:
		print("Wrong Input")

def repeat(times, f):
	for i in range(times):
		f()
	print('player 1 has won ', count1 , 'many times')
	print('player 2 has won ', count2, 'many times')
	print('tie has occur ', count3, 'times')
if __name__ == '__main__':
	repeat(100000, func)
