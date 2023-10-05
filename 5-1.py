n = int(input("Введіть розмір масиву: "))

array = []

for i in range(n):
    element = int(input(f"Введіть {i+1}-й елемент масиву: "))
    array.append(element)

print("Додатні елементи масиву:")

for element in array:
    if element > 0:
        print(element)
