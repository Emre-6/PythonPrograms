numbers=[4,6,9,10,35,57,89,125,244]

#for i in numbers:
#    print(i)

#i=0
#while(i<len(numbers)):
#    print(numbers[i])
#    i+=1

#while numbers:
#    print(numbers.pop(0))

#print(numbers)    

#start=int(input('start: '))
#finish=int(input('finish: '))

#i=start

#while i<finish:
#    i+=1
#    if(i%2==1):
#        print(i)

#i=100

#while(i>0):
#    print(i)
#    i-=1

numbers=[]
i=0
while(i<5):
    number=int(input('number: '))
    numbers.append(number)
    i+=1
numbers.sort()
print(numbers)    
