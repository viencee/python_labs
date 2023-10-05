def remove_duplicates(input_list):
    unique_list = []

    for item in input_list:
         if item not in unique_list:
            unique_list.append(item)

    return unique_list

input_list = input("Введіть список чисел: ").split()
input_list = [int(item) for item in input_list]

unique_list = remove_duplicates(input_list)

print("Список без повторів:", unique_list)
