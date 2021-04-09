secret_number=6
guess_count=0
guess_limit=3
while guess_count<guess_limit:
	guess=int(input("Guess |\t"))
	guess_count += 1
	if guess==secret_number:
		print("You won ")
		break
	