# -*- coding: utf-8 -*-

"""Использование оператора with для автоматического закрытия файла"""

import os.path

# Построение имени файла
filename = os.path.join('data', 'file.txt')

# Оператор with автоматически закроет файл при окончании выполнения операторов
# внутри него или возникновении исключения
with open(filename) as file:
    print(file.read())
