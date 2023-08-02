# global scope
x='global x'

def function():
    #local scope
    #x='local x'
    print(x)

function()
print(x)

###########

name='James'

def changeName(new_name):
    global name
    name=new_name
    print(name)

changeName('Henry')
print('name')

############

name='global string'

def greeting():
   # name='James'

    def hello():
        #name='Henry'
        print('hello'+name)

    hello()

greeting()

########

x=50
def test():
    global x
    print(f'x: {x}''')

    x=100
    print(f'changed x to {x}')

test()
print(x)

