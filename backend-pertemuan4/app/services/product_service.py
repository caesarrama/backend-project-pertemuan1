from app.repositories.product_repo import (
    get_all_products,
    add_product
)


def get_products():
    return get_all_products()


def create_product(data):
    if not isinstance(data, dict):
        return None, "Data harus berbentuk JSON object"

    name = data.get("name")
    price = data.get("price")

    if not isinstance(name, str) or not name.strip():
        return None, "Nama produk wajib diisi"

    if isinstance(price, bool) or not isinstance(price, (int, float)):
        return None, "Harga harus berupa angka"

    if price <= 0:
        return None, "Harga harus lebih dari 0"

    product = {
        "name": name.strip(),
        "price": price
    }

    return add_product(product), None