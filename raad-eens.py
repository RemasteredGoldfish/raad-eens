#SETUP
import random
import time


guess = 0

print('what is thy name noble stranger? ')
myName = input()


Generate = random.randint(1, 1000)
print('well well, ' + myName + ', I got a number in my head between 1 and 10/1000.')
time.sleep(3)
print('Can you guess the Generate wat is in my head?! ')
time.sleep(3)
print(Generate)

#Guessing

while guess  < 10:
    for i in range(10):
        print('')
        GuessNumber = input()
        GuessNumber = int(GuessNumber)

        guess = guess + 1

        if GuessNumber < Generate:
        if GuessNumber != Generate and Generate in range(Generate - 20, Generate + 20):
        if GuessNumber != Generate and Generate in range(Generate - 50, Generate + 50):
            print('You guess too low noble stranger...')
            print('you are close kid! ')
        if GuessNumber > Generate:
            print('you guess it too high noble stranger...')
            print('you are getting closer ')
        if guess == Generate:
            break

    if GuessNumber == Generate:
        guess = str(guess)
        print('you did good, noble stranger...\nyou guess ' + guess + '... took u a while...\n')

    if GuessNumber != Generate:
        Generate = str(Generate)
        print('Nope. That is wrong you kind stranger... the Generate was ' + Generate)

    repeat = int(input('Want another round noble stranger...? '))
    if repeat == 'yes':
        print('too bad')
    else:
        quit()
