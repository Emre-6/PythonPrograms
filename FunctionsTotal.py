def total():
    return 10+20

result=total()+50

def now():
    import datetime
    datetime.datetime.now().year

def ageCalculation():
    return now()-1990

result=ageCalculation()

def hour():
    import datetime
    return datetime.datetime.now().hour

def hello():
    if(hour<12):
        return "Good Morning"
    else:
        return "Hello"
    
result=hello()


print(result)

