def hangman(word):
	wrong = 0
	stages = [
		'________        ',
		'|               ',
		'|        |      ',
		'|        0      ',
		'|       /|\     ',
		'|       / \     ',
		'|               '
	]
	rletters = list(word)
	board = ['_'] * len(word)
	win = False
	print('Welcome to the execution!')
	while wrong < len(stages) - 1:
		print('\n')
		msg = 'Type a letter: '
		char = input(msg)
		if char in rletters:
			cind = rletters.index(char)
			board[cind] = char
			rletters = '$'
		else:
			wrong += 1
		print((' '.join(board)))
		e = wrong + 1
		print('\n'.join(stages[0:e]))
		if '_' not in board:
			print('You win! The hidden word was: ')
			print(''.join(board))
			win = True
			break
		if not win:
			print('\n'.join(stages[0:wrong]))
			print('You lose! The hidden word was: {}'.format(word))

hangman('кот')