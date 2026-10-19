products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 12500000
    },
    {
        "id": 2,
        "name": "Mouse Wireless",
        "price": 250000
    }
]


def get_all_products():
    return products


def add_product(product):
    product["id"] = max(
        (item["id"] for item in products),
        default=0
    ) + 1

    products.append(product)
    return product