def manipulate_list():
    input_list = input("Введіть список чисел: ").split()
    
    input_list = [int(item) for item in input_list]
    
    left_element = int(input("Введіть число для додавання зліва: "))
    right_element = int(input("Введіть число для додавання справа: "))
    
    input_list.insert(0, left_element)  
    input_list.append(right_element)    
    
    print("Список після додавання з обох кінців:", input_list)

manipulate_list()
