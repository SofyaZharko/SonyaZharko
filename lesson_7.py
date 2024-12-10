def read_last(lines, file):
    abstract_file = open(file, 'r', encoding='utf-8')
    row = abstract_file.readlines()
    con = row[lines:]
    for i in row[lines:]:
        print(i)

a = 'article.txt'
line = int(input('Введите целое положительное число '))
tfile = open(a, 'r', encoding='utf-8')
list_number = len(tfile.readlines())

if line > 0 and line < list_number:
    read_last(line, a)





def print_docs(directory):
    all_files = os.walk(directory)
    print(all_files)

print_docs('C:/Users/Vlad/Documents')





def longest_words(file):
    min = 0
    abstract_file = open(file, 'r', encoding='utf-8')
    row = abstract_file.readlines()
    for i in row:
        for j in i.split(' '):
            if len(j) > min:
                min = len(j)
    for i in row:
        for j in i.split(' '):
            if len(j) == min:
                print(j)

a = 'article.txt'
longest_words(a)





file = input('Введите название файла: ')
a = f'{file}.txt'
tfile = open(a, 'w', encoding='utf-8')
text = input('Введите текст: ')
while text != '':
    tfile.write(text + '\n')
    text = input('Введите текст: ')





    import csv
import time
from datetime import datetime

# Открываем файл для записи
with open('rows_300.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Записываем заголовки
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    
    # Генерируем данные
    for i in range(1, 301):
        current_time = datetime.now()
        second = current_time.second
        microsecond = current_time.microsecond
        
        # Записываем данные в файл
        writer.writerow([i, second, microsecond])
        
        # Приостанавливаем выполнение на 0,01 секунды
        time.sleep(0.01)





import os
import random
from PIL import Image, ImageDraw # type: ignore

def circles_generator(num_of_circles=100):
    # Создаем директорию, если она не существует
    os.makedirs('circles', exist_ok=True)

    for i in range(num_of_circles):
        # Генерируем случайный цвет
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        # Создаем изображение
        img = Image.new('RGB', (600, 600), 'white')
        draw = ImageDraw.Draw(img)
        
        # Рисуем круг
        draw.ellipse((150, 150, 450, 450), fill=color)
        
        # Сохраняем изображение
        img.save(f'circles/circle_{i + 1}.jpg')

# Вызов функции
circles_generator()

