products=[
        {'name':'Iphone 9','price':'4000'},
        {'name':'Iphone 10','price':'5000'},
        {'name':'Iphone X','price':'6000'},
        {'name':'Iphone XR','price':'7000'},
        {'name':'Iphone 11','price':'8000'},
        {'name':'Samsung S10','price':'9000'},
    ]


total=0
for product in products:
    total=total+int(product['price'])
print('Product Total: {total} TL')

for product in products:
    if(int(product['price'])>=6000):
       print(f'product name:{product["name"]} product price:{product["price"]}')

word=input('product what do you want:')

for product in products:
    if(product['name'].find(word.lower())>-1):
        print(product['name'])




