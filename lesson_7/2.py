'''
Запросить фразу состоящую минимум из трех слов. 
Сформировать фразу из этих слов в которой каждая буква слова, 
продублирована то количество раз, которое соответствует номеру позиции 
данной буквы в слове этой буквы. 
Например: Привет как дела => Прриииввввееееетттттт кааккк деелллаааа

'''

phrase = input("Введите фразу минимум из трех слов: ")

words = phrase.split()      
new_words = []              

for word in words:
    new_word = ""           
    for i, ch in enumerate(word, start=1):
        new_word += ch * i  
    new_words.append(new_word)

result = " ".join(new_words)   
print(result)