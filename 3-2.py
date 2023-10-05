word1 = input("Введіть перше слово: ")
word2 = input("Введіть друге слово: ")

letters1 = set(word1)
letters2 = set(word2)

unique_letters = letters1.symmetric_difference(letters2)

print("Літери, які зустрічаються в обох словах тільки один раз:", unique_letters)
