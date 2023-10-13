#sumInputs.py

total_round = 0
sentinal = 0
sum_up = 0

while sentinal < 2:
	temp = input()
	total_round += 1
	if temp.isdigit():
		sum_up += int(temp)
		sentinal = 0
	else:
		sentinal += 1

print(total_round * sum_up)
