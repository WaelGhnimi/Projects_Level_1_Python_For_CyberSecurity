#Guess the number
import random
NumOfGuesses = 0

print("Hello, what is your name ?")
name = input()

number = random.randint(1,20)
print("============= You have just 5 chances to try ! ===================")
print("Number I am thinking of is between is between 1 and 20")

while NumOfGuesses < 6:
    print("Take a Guess.")
    guess = int(input())
    
    NumOfGuesses +=1
    if guess < number:
        print("Number is too low")
    if guess > number:
        print("Number is too high")
    if guess == number:
        break
if guess == number:
    print("Well done",name,"you guessed the number in: ",NumOfGuesses);

if guess != number:
    print("Wrong! Unluckly, the number was",number)