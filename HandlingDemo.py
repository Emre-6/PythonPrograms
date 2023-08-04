liste=["1","2","5a","10b","abc","10","50"]

#for x in list:
#    try:
#        result=int(x)
#        print(result)
#    except ValueError:
#        continue

#while True:
#    number=input('number: ')
#    if(number=='q'):
#        break
    
#    try:
#        result=float(result)
#        print(f'Entered Number: {result}')
#        break
#    except ValueError:
#        print('Invalid Number.')
#        continue

d={"ProductName":"Samsung s10"}

def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None

print(get(product,'Price'))
print(get(product,'ProductName'))

