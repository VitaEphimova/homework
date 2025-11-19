'''
Запросить количество секунд. 
Вывести на экран время в формате ЧЧ:ММ:СС равное эти секундам.
Пример: 35457 -> 09:50:57
Сделать 2 варианта с форматной строкой и без.

'''

secundall=int(input(">>>: "))
hours=secundall // 3600
secunds=secundall-hours*3600
minutes=secunds // 60
secunds=secunds-minutes*60
print(f"{secundall} -> {hours:02}:{minutes:02}:{secunds:02}")