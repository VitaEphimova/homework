"""
Запросить у учителя оценки ученика по одной до тех пор пока он не введет 0. 
Выдать средний бал ученика.

"""

total = 0       
count = 0       

while True:
    grade = int(input("Введите оценку ученика (0 — закончить): "))

    if grade == 0:   
        break

    total += grade  
    count += 1       

if count > 0:
    print("Средний балл ученика:", total / count)
else:
    print("Оценок не было введено.")