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

import random
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
    print('No, the number I was thinking of was '+str(secretNumber)+'')











