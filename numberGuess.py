guess = 7
total_round = int(input())
count = 0

while count < total_round:
	temp = int(input())
	if temp == guess:
		print("correct")
		exit()
	count += 1
	if temp > 7:
		print("the guess is too high")
	else:
		print("the guess is too low")

print("you lose")
