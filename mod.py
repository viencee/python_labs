def calculate_product(n):
    if n <= 0:
        print("n має бути натуральним числом")
        return None

    product = 1
    for i in range(2, 2 * n + 1, 2):
        product *= i

    return product
