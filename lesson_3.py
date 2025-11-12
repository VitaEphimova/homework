bufer1=input("Введи строку 1: ")
bufer2=input("Введи строку 2: ")
bufer3=input("Введи строку 3: ")

print(f"{bufer1} {bufer2} {bufer3}\n{bufer1}:{bufer2}:{bufer3}\n - {bufer1}\n - {bufer2}\n - {bufer3}")


number=int(input("Введи число: "))
stepen=int(input("Введи степень: "))
result=number ** stepen
print(result)

telephone=float(input("цена закупки телефона: "))
reteal_cost=telephone*1.3
print(f"{reteal_cost}")
print(f"{reteal_cost*0.95}")
print(f"{reteal_cost*0.90}")
print(f"{reteal_cost*0.85}")

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

secundall=int(input(">>>: "))
hours=secundall // 3600
secunds=secundall-hours*3600
minutes=secunds // 60
secunds=secunds-minutes*60
print(f"{secundall} -> {hours:02}:{minutes:02}:{secunds:02}")

ful1=float(input("число1"))
ful2=float(input("число2"))
ful3=float(input("число3"))
print(f"{((ful1+ful2+ful3)/3):.3f}")
