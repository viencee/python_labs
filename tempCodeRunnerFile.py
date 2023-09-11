# варіант 7

N = int(input("Введіть ціле число N (1<N<9): "))

if N < 2 or N > 8:
    print("Некоректне число N. Введіть число в межах 2-8.")
    
else:
    for i in range(1, N + 1):
        # Генеруємо рядок чисел від i до N та виводимо його
        row = " ".join(map(str, range(i, N + 1)))
        print(row)