'''
Программа должна запросить несколько цифр через пробел 
    - выдать их общую сумму
    - выдать максимальную цифру
    - выдать среднее арифметическое

'''

chisla=input("несколько чисел через пробел: ")
nums = list(map(float, chisla.split()))
allnums = sum(nums)
maximum = max(nums)
average = allnums / len(nums)
print(f"Сумма: {allnums}")
print(f"Максимум: {maximum}")
print(f"Среднее арифметическое: {average}")