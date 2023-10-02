import math

from mod import calculate_product

n = int(input("Введіть натуральне число n: "))
product = calculate_product(n)
if product is not None:
    print(f"Результат обчислення добутку: {product}")
