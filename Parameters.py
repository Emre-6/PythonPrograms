def hello():
    return "Hello,"+ name

result=hello("Sergio")
result=hello("Joao")

def total(a,b):
    return a+b

result=total(10,20)
result=total(20,30)

def ageCalculate(birthyear,name):
    return 2023-birthyear

result=ageCalculate(1990)
result=ageCalculate(1990)

def retireyear(birthyear,name):
    age=ageCalculate(birthyear)

    retire=65-age

    if retire>0:
        print(f"{name},retire time is {retire} year")
    else:
        print(f"{name}, {retire} you are still retire.")
            
ageCalculate(1990,"Sergio")
ageCalculate(1960,"Joao")



print(result)

