numbers=[1,5,7,45,25,96]
alphabet=['A','V','C','E']
names=['Adam','Violet','Charles','Emily']

result=min(numbers)
result=max(numbers)

result=min(alphabet)
result=max(alphabet)

result=min(names)
result=max(names)

result=min([len(names) for name in names])
result=max([len(names) for name in names])

result=max(names,key=lambda n: len(n))
result=min(names, key=lambda n: len(n))

product=[
    {"title":"Iphone x","Price":5000},
    {"title":"Iphone xr","Price":6000},
    {"title":"Iphone 11","price":7000}
]

result=min(products,key=lambda product: product['Price'])
result=min(products,key=lambda product: product['Price'])['Title']
result=max(products,key=lambda product: product['Price'])['Title']

max=0

for product in products:
    if product["price"]>max:
        max=product["price"]

print(max)
