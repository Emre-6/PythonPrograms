def values(a,b):
    if(a>b):
       return " a is bigger than b"
    elif(b>a):
        return "b is bigger than a"
    return "a is equal to b"

result=values(a=10,b=20)
print(result)

def findcharacternumber(s):
    return { letter for letter in string }
    
result=findcharacternumber("Flutter")

def update_list(list,command,position,value=None):
    if(command=="remove" and position=="end"):
        return list.pop()
    elif(command=="remove" and position=="beginning"):
        return list.pop(0)
    elif(command=="add" and position=="end"):
        list.append(value)
    elif(command=="add" and position=="beginning"):
        return list

result=update_list([1,2,3],"add","end",4)
result=update_list([1,2,3],"add","beginning",4)
result=update_list([1,2,3],"remove","beginning")
print(result)


def contains_blue(*args):
    if "blue" in args:
        return True
    return False

result=contains_blue("blue","yellow","red")
result=contains_blue("blue","yellow","red")

print(result)



