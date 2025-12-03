"""
1. Запросить у пользователей имя и отзыв о магазине. 
Программа должна запрашивать данные пока не введено слово "stop". 
Все данные сложить в словарь.
    -распечатать количество отзывов
    -распечатать отдельно имена пользователей
    -распечатать отдельно отзывы

"""

reviews = {}   # словарь: имя → отзыв

while True:
    name = input("Введите имя (или stop для выхода): ").strip()
    if name.lower() == "stop":
        break

    review = input("Введите отзыв: ").strip()
    if review.lower() == "stop":
        break

    reviews[name] = review   # добавляем запись в словарь

# 1. Количество отзывов
print("Количество отзывов:", len(reviews))

# 2. Имена пользователей
print("Имена пользователей:")
for name in reviews.keys():
    print(name)

# 3. Отзывы
print("Отзывы:")
for review in reviews.values():
    print(review)