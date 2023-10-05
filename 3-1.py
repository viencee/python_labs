input_string = input("Введіть довільний рядок: ")

if len(input_string) >= 6:
    result = input_string[-6:-2]
    print("Потрібна послідовність символів:", result)
else:
    print("Рядок занадто короткий для виконання операції зрізу.")
