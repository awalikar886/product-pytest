from product import product_details

def test_product_details():
    expected_output = (
        "Product ID: P101\n"
        "Product Name: Laptop\n"
        "Quantity: 2\n"
        "Price: 55000\n"
    )

    assert product_details("P101", "Laptop", 2, 55000) == expected_output