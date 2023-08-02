def hello(name="User",message="Have a Nice Day"):
    print(f"{message}{name}")

hello("Harry","Good Morning")
hello("Harry","Have a Nice Day")
hello("Harry")
hello()

def Number(number1,number2):
    return number1**number2

result=Number(2,3)
result=Number(3,3)

def total(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

def calculation(a,b,fn=total):
    return fn(a,b)

result=calculation(5,3,subtraction)
    
print(result)


