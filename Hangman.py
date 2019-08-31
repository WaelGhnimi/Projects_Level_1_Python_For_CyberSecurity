#Hangman
import random

AnswerList = ["world","look","hello","goodbye"]

random.shuffle(AnswerList)
answer = list(AnswerList[0])

display = []

display.extend(answer)

for i in range(len(display)):
	display[i] = "_"

print(' '.join(display))

count = 0
while count < len(answer):
	guess = input("Please guess a letter: ").lower()
	print(count)

	for i in range(len(answer)):
		if answer[i] == guess:
			display[i] = guess
			count +=1


	print(''.join(display))
	print()

print("Well done, you guessed the word")
