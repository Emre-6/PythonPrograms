i=0
amount=int(input('Add the amount of product'))
products=[]

while(i<amount):
    productName=input('product name:')
    price=input('product price:')
    products.append({'ProductName':productName,'Price':price})
i += 1

#for product in products:
#    print(f"Product Name:{product['ProductName:']} Product Price:{product['price']}")


a=0
while(a<len(products)):
    print(f"Product Name:{products[a]['productname']} product price:{products[a]['price']}")
    a+=1
    