import db

def AddProduct():
    db.products.append({
        "id": len(db.products)+1,
        "ProductName": productname,
        "Price": price
    })

def ProductUpdate(id,productName,Price):
    for product in db.products:
        if(product["id"]==id):
            product["productname"]=productName
            product["Price"]=Price
            break
def productsBring():
    for product in db.products:
        print(f"id {product['id']} product name: {product['productName']} price:{product['price']}")
