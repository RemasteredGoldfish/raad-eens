import random
Generate = random.randint(1,1000)
tries = 0

myName = input('What is your name noble stranger... ')
print('well well, ' + myName + ', I got a number in my head between 1 and 10/1000.')
print('Can you guess the Generate wat is in my head?! ')
print(Generate)

guessNumber = input()
guessNumber = int(guessNumber)
tries +=1
for i in range(10):
    if guessNumber > Generate:
        print('Guess Lower...')
    if guessNumber < Generate:
        print('Guess Higher...')

    while guessNumber != Generate and tries <10:
        guessNumber = input('Try again: ')
        guessNumber = int(guessNumber)
        tries += 1

    if guessNumber > Generate:
        print('Guess Lower...')
    if guessNumber > Generate and Generate < guessNumber -20:
        print('Your warm')
    if guessNumber < Generate:
        print('Guess Higher...')

    if guessNumber == Generate:
        print('congrats! ')
        print(f'Number of tries: {tries}')
    else:
        print('congrats u lost "fukkin bot >.>"')

