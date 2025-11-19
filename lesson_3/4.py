'''
запросить число и вывести на экран сколько номиналов в этом числе:
	 - тысячи
	 - сотни
	 - десятки
	 - единицы

пример: # знак >>> значит что ввели что-то через input
    >>> 21234 
    тысяч - 21
    сотни - 2
    десятки - 3
    единицы - 4
'''

number4=int(input(">>>>>>>>: "))
num1000=number4 // 1000
print(num1000) 
number4=number4-num1000*1000
num100=number4 // 100
print(num100)
number4=number4-num100*100
num10=number4 // 10
print(num10)
number4=number4-num10*10
print(number4)