import re
fraza=input("ввидите фразу: ")
chars = len(fraza)
words = len(re.findall(r"\S+", fraza))
vowels = len(re.findall(r"[aeiouаеёиоуыэюя]", fraza, flags=re.IGNORECASE))
print(f"Символов: {chars}")
print(f"Слов: {words}")
print(f"Гласных: {vowels}")

chisla=input("несколько чисел через пробел: ")
nums = list(map(float, chisla.split()))
allnums = sum(nums)
maximum = max(nums)
average = allnums / len(nums)
print(f"Сумма: {allnums}")
print(f"Максимум: {maximum}")
print(f"Среднее арифметическое: {average}")


word = input("Введите слово: ")
print(word[::-1])


s = "имя: Дмитрий, фамилия: Иванов, возраст: 18"
parts = s.split(", ")
data = {}
for part in parts:
    key, value = part.split(": ")
    data[key] = value
    name = data["имя"]
surname = data["фамилия"]
age = data["возраст"]
print(name, surname, age, sep="\n")
