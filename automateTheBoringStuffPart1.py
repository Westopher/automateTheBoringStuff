""" print('hello world')
print('What is your name?')
myName = input()
print("It's good to meet you" + myName)
print("The length of your name is:")
print(len(myName))
print("What is your age?")
myAge = input()
print("You will be " + str(int(myAge) + 1) + ' in a year.')
 """

""" bacon = 20

print(bacon + 1)

rounded = round(6.2094532708376, 2)
print(rounded)

print("I have eaten " + str(99) + " burritos")

spam = 0
while spam < 5:
    print("hey,hey,hey")
    spam = spam + 1 """

""" while True:
    print("Who dat boy? Who him is?")
    name = input()
    if name != 'West':
        continue
    print("Hello West, What's the password?")
    password = input()
    if password == 'password':
        break
print("access granted") """

""" print("my name is")

for i in range(5):
    print('West '+str(i)+' is the number') """

""" total = 0
for num in range(101):
    total = total + num
    print(''+str(num)+' is the number. '+str(int(total))+' is the current total')
print(total) """


""" 
for i in range(5):
    print(random.randint(1, 10)) """

""" while True:
    print("Type exit to exit")
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed '+ response +'.') """

""" import random
secretNumber = random.randint(1,20)
print("Choose a number between 1 and 20.")

for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print("Too low")
    elif guess > secretNumber:
        print("Too high")
    else:
        break

if guess == secretNumber:
    print('You got it. The number was '+str(secretNumber)+'. It took you '+str(guessesTaken)+' guesses')
else:
    print('No, the number I was thinking of was '+str(secretNumber)+'') """

import random, sys

print('Rock, Paper, Scissors')

wins = 0
losses = 0
ties = 0

while True: #main game loop
    print('%s Wins, %s Losses, %s Ties' %(wins, losses, ties))
    while True: #player input loop
        print('Shoot your shot: (r)ock, (p)aper, (s)cissors, or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() #leave the game / end the program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break #leave the input loop

    if playerMove == 'r':
        print('Rock vs...')
    if playerMove == 'p':
        print('Paper vs...')
    if playerMove == 's':
        print('Scissors vs...')

    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('Rock')
    elif randomNumber == 2:
        computerMove = 'p'
        print('Paper')
    elif randomNumber == 3:
        computerMove = 's'
        print('Scissors')
    
    if playerMove == computerMove:
        print('It is a tie, shoot again.')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win.')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1







