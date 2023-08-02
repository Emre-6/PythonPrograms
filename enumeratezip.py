brands=["Opel","BMW","Mercedes"]

#index=0
#for brand in brands:
#    print(f"{index+1}-{brands[index]}")
#    index+=1

#obj1=enumerate(brands)

#print(type(obj1))
#print(list(obj1))

#for index,value in enumerate(brands):
#    print(f"{index}-{value}")

#zip

#liste1=[1,2,3,4,5]
#liste2=['a','b','c','d','']

#print(list(zip(liste1,liste2)))

#for item in zip(liste1,liste2):
#    print(item)

#for a,b,c in zip(liste1,liste2,liste3):
#    print(a,b,c)

#for i in range(1,1):
#    print('*********')
#    for k in range(1,11):
#        print("{} x {}={}".format(i,k,i*k))

number=int(input('number: '))

private=True

if(number==1):
    private=False

for i in range(2,number):
    if(number%i==0):
        private=False
        break

if private:       
    print('Number is private')
else:
    print('Number is not private')
    
        
