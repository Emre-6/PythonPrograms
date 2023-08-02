#name=input('name:')
#age=int(input('age:'))
#graduate=input('Graduate:')

#if(age>=18): 
#    if(graduate=='High School'or graduate=='University'):
#     print('You can take driving licence')
#    else:
#     print(f'{name} You cant take driving licence' )    
#else:
#    print(f'{name}Your age is not enough to take driving licence')

#exam1=float(input('1.exam:'))
#exam2=float(input('2.exam'))
#project=float(input('project'))

#average=(exam1+exam2+project)/3

#if(average>=0) and (average<25):
#    print(f'average:{average} and grade: 0')
#elif(average>=25) and (average<45):
#    print(f'average:{average} and grade: 1')
#elif(average>=45) and (average<55):
#    print(f'average:{average} and grade 2')
#elif(average>=55) and (average<70):
#    print(f'average:{average} and grade 3')
#elif(average>=70) and (average<85):
#    print(f'average:{average} and grade 4')
#elif(average>=85) and (average<=100):
#    print(f'average:{average} and grade 5')

import datetime

date=input('Car started to drive 07/11/2023')
date=date.split('/')

now=datetime.datetime.now()
drive=datetime.datetime(int(date[0]),int(date[1]),int(date[2]))

division=now-drive
day=division.days

if(day<=365):
    print('1.service:')
elif(day>365) and (day<=365*2):
    print('2.service:')
elif(day>=365*2) and (day<=365*3):
    print('3.service:')
else:
    print("Information is false")       





    