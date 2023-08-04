numbers=[1,2,3,4,5,6]
str_numbers=["1","2","3","4","5","6"]
names=["Johnny","Hans","Tony","Mary"]
users=[{"Name":"Johnny","Surname":"Deep"},{"Name":"Johnny","Surname":"Deep"}]
#square=[]

#for number in numbers:
#    square.append(number**2)

#print(square)

#def TakePowerofTwo():
#    return number **2

result=list(map(lambda number: number **2, numbers))
result=list(map(int,str_numbers))
result=list(map(abs,numbers))
result=list(map(abs,numbers))
result=list(map(len,names))
result=list(map(str.capitalize,names))
result=list(map(lambda x: x["ad"],users))


print(result)


    