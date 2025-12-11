def product_details(product_id, name, quantity, price):
    result = (
        f"Product ID: {product_id}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}\n"
    )
    return result


if __name__ == "__main__":
    # Example call
    print(product_details(101, "Laptop", 5, 55000))
