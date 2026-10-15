import os
import time
import math

def clear():
    os.system("cls" if os.name == "nt" else "clear")
WHITE = '\u001b[47m'
RED = '\u001b[41m'
ERASE = '\u001b[0m'
DARK = "\u001b[40m"  

width = 15
height = 3

print("Флаг Польши")
for stripe in range(height):
    print(WHITE + " " * width + ERASE)
for stripe in range(height):
    print(RED + " " * width + ERASE)


time.sleep(3)

print("Повторяющийся узор")

LENGHT = 24
HIGHT = 5 #нечетное число
for line in range(HIGHT):
    if line%2==0:
        print(f'{WHITE}{" "*LENGHT}{ERASE}')
    elif line%5==1:
        print((f'{" " * 8}{WHITE} {ERASE} ')*(LENGHT//10))
    else:
        print((f'   {WHITE} {ERASE}      ')*(LENGHT//10))

print('-'*70)
time.sleep(3)


print("Анимация")
def animation():
    for i in range(4):
        clear()
        print(" " * (i * 3) + "O")
        time.sleep(1)
animation()

print("Диаграмма")


with open("sequence.txt", "r") as file:
    numbers = [float(line) for line in file]

first = numbers[:125]
second = numbers[125:250]

avg1 = sum(abs(x) for x in first) / len(first)
avg2 = sum(abs(x) for x in second) / len(second)

total = avg1 + avg2

percent1 = avg1 / total * 100
percent2 = avg2 / total * 100

print("Первые 125 чисел:", round(percent1, 2), "%")
print("Вторые 125 чисел:", round(percent2, 2), "%")

print("\nДиаграмма:")
print("Первые: ", "#" * round(percent1), f"{percent1:.2f}%")
print("Вторые: ", "#" * round(percent2), f"{percent2:.2f}%")
time.sleep(0.5)



