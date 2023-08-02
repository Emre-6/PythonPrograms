#def displayUser(*args):
#    print(type(args))
#    print(args)

#displayUser()

def displayUser():
    for key, value in kwargs.items():
        print(f"{key}:{value}")
    print(type(kwargs))
    print(kwargs)

displayUser(username="AanakinSkywalker")
displayUser(usename="AnakinSkywalker",email="sw@anakin.com")
displayUser(username="AnakinSkywalker",email="sw@anakin.com",country="Tatoine")    

def myFunction(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,key1="value 1",key2="value 2")

