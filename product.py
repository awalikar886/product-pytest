def product_details(product_id, name, quantity, price):
    result = (
        f"Product ID: {product_id}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}\n"
    )
    return result


if _name_ == "_main_":
    product_id = "P101"
    name = "Laptop"
    quantity = 2
    price = 55000
    print(product_details(product_id, name, quantity, price))