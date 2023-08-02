#number=int(input('number: '))
#if(number>50) and (number<=100):
#    print(f"{number}, 50 to 100")
#else:
#    print(f"{number}, Not 50 to 100")

#number=int(input('number: '))
#if(number>0):
#    if(number%2==1):
#        print('Positive Add Number:')
#    else:
#        print("Positive but not add number:")    
#else:
#    print("Negative Number.")    

#x=int(input('x: '))
#y=int(input('y: '))
#z=int(input('z: '))

#if(x>y) and (x>z):
#  print("x is the biggest number")

#if(y>x) and (y>z):
#  print("y is the biggest number")

#if(z>x) and (z>y):
#  print("z is the biggest number")  

#midterm1=float(input('midterm1: '))
#midterm2=float(input('midterm2: '))
#final=float(input('final: '))

#average=(((midterm1+midterm2)/2)*0.4)+(final*0.6)

#result=(average>=50)or(final>=70)

#print(f"Student grade average:{average} and passorfail:{result}")

#if(average>=50):
#    print(f'Student Grade Average: {average} and student pass')
#else:
#    if(final>=70):
#        print(f'Student grade average: {aaverage} and student is successful')
#    else:
#        print(f'student grade average:{average} and student failed.')

name=input('Name: ')
kg=float(input('Weight:'))
hg=float(input('Height:'))

kiloIndeks=kg/(hg**2)

weak=(kiloIndeks>=0) and (kiloIndeks<=18.4)
normal=(kiloIndeks>18.4) and (kiloIndeks<=24.9)
fat=(kiloIndeks>24.9) and (kiloIndeks<=29.9) 
bigsize=(kiloIndeks>=29.9)and(kiloIndeks<=34.9)

if(weak):
    print(f"{name} weight index:{kiloIndeks} weak")
elif(normal):
   print(f"{name} weight index:{kiloIndeks} normal")
elif(fat):
  print(f"{name} weight index:{kiloIndeks} fat")
elif(bigsize):
   print(f"{name} weight index:{kiloIndeks} bigsize")
else:
   print("Informations are false.")            
