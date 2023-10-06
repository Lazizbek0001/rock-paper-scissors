from random import randint



choice = ''

while choice != 'n':
	number_roun = int(input("How many rounds: "))

	player_wins = 0

	ai = 0

	rounds = 0

	while roun < number_roun:
		player = input("Choose: ").lower()
		roun +=1
		num = randint(1,3)
		print(f"Round: #{rounds}")
		if num == 1:
			move='rock'
		elif num == 2:
			move = 'paper'
		else:
			move = 'qaychi'
		print(f"Ai has chosen {move}")
		if move == player:
			print("Draw")

		elif move == 'rock' and player == 'paper':
			print("Player win")
			pw +=1

		elif move == 'rock' and player =='scissors':
			print("AI win")
			ai +=1

		elif move == 'paper' and player == 'rock':
			print("AI win")
			ai +=1

		elif move == "paper" and player == 'scissors':
			print("Player win")
			pw +=1

		elif move == 'scissors' and player == 'rock':
			print("Player win")
			pw +=1

		elif move == 'scissors' and player == 'paper':
			print("AI win")
			ai +=1

		print(f"Total: {player_wins}:{ai}")
		

	if player_wins > ai:
		print(f"Overall Player wins: {player_wins}:{ai}!")
	elif pw == ai:
	    print(f"Overall Draw: {player_wins}:{ai}!!!")
	else:
	    print(f"Overall Computer wins: {player_wins}:{ai}!")

	choice = input("Do you want to play again (y/n): ")
