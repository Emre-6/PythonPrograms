#list=[10,20,30]

#def total(numbers):
#    result=0
#    for i in numbers:
#        result+=i
#    return result

def total(*args):
    print(type(args))
    print(args)
    result=0
    for i in args:
        result+=i
    return result


print(total(10,20,30))
print(total(10,20,30,40))

a=10,20,30

for i in a:
    print(i)
print(a)





