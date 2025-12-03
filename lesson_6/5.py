"""
Запросить фразу 
    - вывести на экран количество уникальных символов
    - вывести на экран количество уникальных слов
    -* вывести символ который встречался чаще всего

"""
fraza= input("ввиидите фразу: ")

unical_simbl= set(fraza)
print("уникальных символов:", len(unical_simbl))

worlds=fraza.split()
unical_slova= set(worlds)
print("уникальных слов:", len(worlds))

