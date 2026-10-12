import os
import time
import math

def clear():
    os.system("cls" if os.name == "nt" else "clear")
WHITE = '\u001b[47m'
RED = '\u001b[41m'
ERASE = '\u001b[0m'
DARK = "\u001b[40m"  
ED = f'{WHITE} {ERASE}' 
width = 15
height = 3

print("Флаг Польши")
for stripe in range(height):
    print(WHITE + " " * width + ERASE)
for stripe in range(height):
    print(RED + " " * width + ERASE)


time.sleep(1)

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
print("Анимация")
frames = [
    "●         ",
    "   ●      ",
    "      ●   ",
    "         ●"
]

for frame in frames:
    clear()
    print(frame)
    time.sleep(0.5)

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



WIDTH = 40
HEIGHT = 12
X_MAX = 16
Y_MAX = math.sqrt(X_MAX)

graph = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]

y_axis = 2
x_axis = HEIGHT - 2
for r in range(HEIGHT):
    graph[r][y_axis] = "|"
for c in range(y_axis, WIDTH):
    graph[x_axis][c] = "-"


for i in range(WIDTH - y_axis - 1):
    x = (i / (WIDTH - y_axis - 2)) * X_MAX
    y = math.sqrt(x)
    row = int(round((1 - y / Y_MAX) * (x_axis - 1)))
    col = y_axis + 1 + i
    if 0 <= row < HEIGHT:
        graph[row][col] = ED

for row in graph:
    print("".join(row))

print('-'*70)
