import math

def expression (m):
    if m == 3:
            print("m не може дорівнювати 3, оскільки знаменник стає рівним нулю.")
            return None
    z = math.sqrt((m + 3)/(m - 3))
    return z

def calculate_product(n):
    if n <= 0:
        print("n має бути натуральним числом")
        return None
    
    product = 1
    for i in range(2, 2 * n + 1, 2):
        product *= i

    return product

m = float(input("Введіть значення m: "))
print ("Значення виразу z = ", expression(m))

n = int(input("Введіть натуральне число n: "))
product = calculate_product(n)
if product is not None:
    print(f"Результат обчислення добутку: {product}")
