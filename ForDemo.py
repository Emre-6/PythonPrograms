numbers=[1,5,15,25,56,74]

#for number in numbers:
#    if(number%5==0):
#        print(number)
total=0
for number in numbers:
 if(number%2==0):
  print(number,number*number)

  # total=total+numbers
#print(total)


 product=['IPhone','Samsung','Huawei','LG']

count=0
for prod in product:
    index=prod.find('IPhone')
    if(index>1):
      count+=1
print(count)




        