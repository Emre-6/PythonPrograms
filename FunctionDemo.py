#def write(txt,amount):
#    print(txt*amount)

#write('Hello\n',5)

#def calculate(long,short):
#    area=long*short
#    perimeter=2*(long+short)

#    print(f"area:{area} perimeter:{perimeter}")

#calculate(5,7)

#def Coin():
#    import random
#    number=random.random()

#    if number>0.5:
#        return "Tails"
#    else:
#        return "Heads"
#print(Coin())

#def primenumber(number1,number2):
#    for number in range(number1,number2):
#        if(number>1):
#            for i in range(2,number):
#                if(number%i==0):
#                    break
#                else:
#                    print(number)

#Findprimenumber(10,20)


def division(number):
    division=[]

    for i in range(2,number):
        if(nummber%i==0):
            division.append(i)
    return division

print(division(15))
print(division(35))                    

