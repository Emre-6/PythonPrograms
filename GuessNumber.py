import random

number=random.randint(1,100)
live=int(input('How many time to use it?:'))
time=5
counter=0
while time>0:
    time-=1
    counter+=1
    guess=int(input('guess: '))

    if number==guess:
        print('Congratulations {counter}. time true answer Total Point: {100-(100/live)*(counter-1)}')
        break
    elif number>guess:
        print('up')
    else:
        print('down')

    if time==0:
        print('Your time is over The guess number:{number}')        
