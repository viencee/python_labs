sentence = input("Введіть речення: ")

words = sentence.split()
words_with_o = []

for word in words:
    if 'о' in word.lower():
        words_with_o.append(word)


if words_with_o:
    print("Слова, які містять хоча б одну літеру 'о':")
    for word in words_with_o:
        print(word)
else:
    print("У реченні немає слів з літерою 'о'.")
