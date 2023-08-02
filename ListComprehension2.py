#for item in lists:
#    if(condition):
#        expression
#[expression for item in list if condition]

for number in numbers:
    if(number%2==0):
        result.append(number)

result=[number for number in numbers if number%2==0]
result=[number if number%2==0 else "Odd Number" for number in numbers]

price=[1000,3000,5000,0,4000]
taxes=[]

for value in price:
    if(value>0):
        taxes.append(price*1.18)

taxes=[price*1.18 for value in rpices if value>0]
taxes=[price*1.18 if value>0 else "taxes can't calculates" for value in prices]

result=[]
for x in range(3):
    for y in range(3):
     result.append((x,y))

result=[(x,y) for x in range(3) for y in range(3)] 
 
print(result)

