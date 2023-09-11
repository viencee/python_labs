# варіант 7
a = int(input ("Ведіть а: "))

while (a < 0 ):
    a = int(input ("Ведіть а: "))

b = int(input ("Ведіть b: "))

while (b < 0):
    b = int(input ("Ведіть b: "))

if a > b:
    r = (a * b + 21)

elif a == b:
    r = -125

else:
    r = (a - 5) / b

print("Результат обчислення виразу: " , r)