# -*- coding: utf-8 -*-

"""Пример использования функции os.path.join
для построения пути к файлу"""

# Модуль, который содержит функции для работы с путями в файловой системе
import os.path

def read_file(fname):
	"""Функция для чтения файла fname
	и вывода его содержимого на экран
	"""

	# Открытие файла для чтения
	file = open(fname, 'r')

	# Вывод названия файла
	print('File ' + fname + ':')

    # Чтение содержимого файла построчно
	for line in file:
		# Вывод строки s.  Перевод строки в файле сохраняется в строке, поэтому
		# выводим без дополнительного перевода строки.
		print(line, end='')

	# Закрытие файла
	file.close()


if __name__ == '__main__':
    # Функция os.path.join соединяет части пути в файловой системе требуемым
    # для данной платформы разделителем
    read_file(os.path.join('data', 'file.txt'))
