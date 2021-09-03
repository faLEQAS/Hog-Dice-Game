import random


def get_input():
	times = input("how many times do u want to play\n")
	while times.isalpha() or int(times) not in range(0,11):
		times = input("invalid choice, please pick a number from 1 to 10\n")
	return int(times);

def roll_dice():
	dice = random.randint(1,6)
	return dice

def track_dice_rolls(dice, listofrolls):
	listofrolls.append(dice)

	return listofrolls

def get_score(listofrolls):
	score = 0

	for i in listofrolls:
		if i == 1:
			score = 1
			break

		score += i

	return score;

def switch_player(player):
	if player == "1":
		return "2"

	return "1"

def add_to_score(player, score, totalplayer1, totalplayer2):
	if player == "1":
		return totalplayer1+score, totalplayer2

	return totalplayer1, totalplayer2+score

def get_first_player():
	player = input("\nWho starts first ?\n")

	while player not in ["1", "2", "1 ", "2 "]:
		print("invalid choice, please type in 1 or 2\n")
		player = input()

	return player;

def check_for_score_swap(totalplayer1, totalplayer2, player):
	if player == "1":
		currentplayer = totalplayer1
		opponentplayer = totalplayer2
	else:
		currentplayer = totalplayer2
		opponentplayer = totalplayer1
	if str(currentplayer)[0] == str(opponentplayer)[::-1][0] and len(str(currentplayer)) != 1 and len(str(opponentplayer)) != 1:
		print("TOTAL SCORES SWAPPED")
		return totalplayer2, totalplayer1

	return totalplayer1, totalplayer2

def zero_times(totalplayer1, totalplayer2, player): #function for handling when the player chooses to roll 0 times, couldn't think of a better name
	total = totalplayer2 if player == "1" else totalplayer1
	if len(str(total)) == 2:
		total = list(str(total))
		minnum = min(total)
		score = 10 - int(minnum)
		return score
	score = 10
	return score



def main():
	totalplayer1 = 0
	totalplayer2 = 0
	player = get_first_player()		

	while totalplayer1 < 100 and totalplayer2 < 100:
		print(f"its {player}'s turn")
		times = get_input()
		print("\n\n")

		if times != 0:

			amountofplays = 0

			listofrolls = []

			while amountofplays < times:
				amountofplays += 1
				dice = roll_dice()
				listofrolls = track_dice_rolls(dice, listofrolls)
				print(f"Roll{amountofplays}: {dice}")
			score = get_score(listofrolls)

		else:
			score = zero_times(totalplayer1, totalplayer2, player)

		print(f"\nScore: {score}\n")
		totalplayer1, totalplayer2 = add_to_score(player, score, totalplayer1, totalplayer2)

		totalplayer1, totalplayer2 = check_for_score_swap(totalplayer1, totalplayer2, player)
		player = switch_player(player)

	print(f"\nPlayer 1: {totalplayer1}\nPlayer 2: {totalplayer2}\n")

main()
