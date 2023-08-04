numbers=[34,3,7,93]

result=sum(numbers)
result=sum(numbers,10)

product=[
    {"Title":"Iphone X","Price":5000,"isActive":True},
    {"Title":"Iphone Z","Price":6000},
    {"Title":"Iphone 10","Price":7000},
    {"Title":"Iphone 11","Price":8000}
]

TotalPrice=sum([product["Price"] for product in products])
productAmount=len([product for product in products if product["Price"]>0])
result=TotalPrice/len(products)

result=round(10.2)
result=round(10.6)
result=round(10.5)
result=round(1.424242,2)
result=round(1.426242,2)
result=round(1.426242,4)

print(result)

