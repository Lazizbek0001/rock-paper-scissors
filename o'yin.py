from random import randint



choice = ''

while choice != 'n':
	number_roun = int(input("How many rounds: "))

	pw = 0

	ai = 0

	roun = 0

	while roun < number_roun:
		p1 = input("Tanlang: ").lower()
		roun +=1
		num = randint(1,3)
		print(f"Round: #{roun}")
		if num == 1:
			move='rock'
		elif num == 2:
			move = 'paper'
		else:
			move = 'qaychi'
		print(f"Ai has chosen {move}")
		if move == p1:
			print("Draw")

		elif move == 'rock' and p1 == 'paper':
			print("Player win")
			pw +=1

		elif move == 'rock' and p1 =='qaychi':
			print("AI win")
			ai +=1

		elif move == 'paper' and p1 == 'rock':
			print("AI win")
			ai +=1

		elif move == "paper" and p1 == 'qaychi':
			print("Player win")
			pw +=1

		elif move == 'qaychi' and p1 == 'rock':
			print("Player win")
			pw +=1

		elif move == 'qaychi' and p1 == 'paper':
			print("AI win")
			ai +=1

		print(f"Total: {pw}:{ai}")
		

	if pw > ai:
		print(f"Overall Player wins: {pw}:{ai}!")
	elif pw == ai:
	    print(f"Overall Draw: {pw}:{ai}!!!")
	else:
	    print(f"Overall Computer wins: {pw}:{ai}!")

	choice = input("Do you want to play again (y/n): ")
	























from random import randint
# i = 0

# while i < 100:
	
# 	if i%2!=0:
# 		print(i)
# 	i+=1

# for i in range(0,30,2):
# 	print(i)

num = randint(1,1000)

my = 0

ron = 0

while num != my:
	my = int(input("Son kiriting: "))
	if my == num:
		print("Topdiz :)")
		print(num)
		
	elif my <num:
		print("Son kichkina :(")
	elif my >num:
		print("Son katta :(")

	ron +=1
print(f"{ron} urinishda topdiz :( ")
