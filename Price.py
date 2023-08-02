oilprice=7.52
diselprice=5.92

oilconsumption=float(input('100 km oil consumption:'))
way=float(input('average distance way:'))
oiltype=input('Type of Oil:')

Total=way*(oilconsumption/100)

if(oiltype=="oil"):
    Total=oilprice*Total
elif(oiltype=="dizel"):
    Total=diselprice*Total
else:
    print('Wrong type of oil')

if(Total!=0):
    print(Total)

