#textBasedAdventure
while True:
	answer = input("Are you ready to play ? (yes/no)")

	if answer.lower().strip() == "yes":

		answer = input("You reach a crossroads, would you like to left or right?").lower().strip()
		if answer == "left":
			answer = input("You encounyer a monster, would you like to run or attack.")

			if answer == "attack":
				print("The was not the greatest idea, you lost!")
			else:
				print("Good choice, you made it away safely")

				answer = input("You see a car and a plane, which would you to tike? (car/plane)")
				if answer == "plane":
					print("Unfortunately you do not know how to fly .. Game over")
				else:
					print("Yes !, you won - you can travel now")
					break


		elif answer == "right":
			print("You walk aimlessly to the right and fall on a patch of ice. You injure your leg and cannot continue, Game Over! ")

	else:
		print(" You quit ! That's to bad!")
		break