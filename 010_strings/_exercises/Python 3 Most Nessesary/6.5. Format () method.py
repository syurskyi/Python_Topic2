# # -*- coding: utf-8 -*-
#
# print("Символы {{ и }} — @".f...("специальные"))
# # Символы { и } — специальные
#
#
# print("@ — @ — @".f... 10 12.3 "string"      # Индексы
# # '10 — 12.3 — string'
# arr = [10, 12.3, "string"]
# print("@ — @ — @".f... $?                    # Индексы
# # '10 — 12.3 — string'
# print(" model — color ".f... c.._ red , m.._ BMW # Ключи
# # 'BMW — red'
# d = "color" "red" "model" "BMW"              # dict
# print(" m.. — c..".f... $$?                  # Ключи
# # 'BMW — red'
# print(" c.. — @".f... 2015 c.._ red         # Комбинация
# # 'red — 2015'
#
#
# arr = [10, [12.3, "string"]]
# print(" 0 0 — 0 1 0 — 0 1 1".f... ?    # Индексы
# # '10 — 12.3 — string'
# print("? 0 — ? 1 1".f...(a.._a..       # Индексы
# '10 — string'
#
#
# c_ Car
#     color, model _ "red", "BMW"
#
#
# car = C..
# print(" 0.m.. — 0.c..".f... ?             # Атрибуты
# # 'BMW — red'
#
#
# print("@ — @ — @ — n".f... 1, 2, 3, n_4  # "{0} — {1} — {2} — {n}"
# # '1 — 2 — 3 — 4'
# print("@ — @ — n — @".f... 1, 2, 3, n_4  # "{0} — {1} — {n} — {2}"
# # '1 — 2 — 4 — 3'
#
#
# print("_$$_".f...("строка"                  # str()
# # строка
# print(" $$_".f...("строка"))                   # repr()
# # 'строка'
# print(" $$_".f...("строка"                   # ascii()
# # '\u0441\u0442\u0440\u043e\u043a\u0430'
#
# Параметр <Ширина> задает минимальную ширину поля. Если строка не помещается
# в указанную ширину, то значение игнорируется, и строка выводится полностью:
# print("' 0 10 ' ' 1 3'".f... 3, "string"
# # "'         3' 'string'"
#
#  Ширину поля можно передать в качестве параметра в методе format (). В этом случае
#  вместо числа указывается индекс параметра внутри фигурных скобок:
# print("' 0 1 '".f...(3, 10 # 10 — это ширина поля
# # "'         3'"
#
# print("' 0 |left|10' ' 1 |right|10' ' 2 |center|10'".f... 3, 3, 3
# # "'3         ' '         3' '    3     '"
#
#
# print("' 0 _10' ' 1 _10'".f... -3 3
# # "'-        3' '         3'"
#
#
# print("' 0 _010' ' 1 _010'".f... -3, 3
# # "'-000000003' '0000000003'"
#
#
# print("' 0 0_10 ' ' 1 0_10 '".f... -3 3
# # "'-000000003' '0000000003'"
# print("' 0 *<10' '1 +>10 ' ' 2 .^10 '".f... 3, 3, 3
# # "'3*********' '+++++++++3' '....3.....'"
#
#
# print("' 0 + ' ' 1 + ' ' 0 - ' ' 1 - '".f... 3, -3
# # "'+3' '-3' '3' '-3'"
# print("' 0 ' ' 1  '".f... 3, -3       # Пробел
# # "' 3' '-3'"
#
# print("' 0 ? ' ' 0 #?'".f... 3  # binar
# # "'11' '0b11'"
#
# print("' 0 ?'".f... 100         # preobrazyet celoe chislo v soootvestvyjychij simvol
# # "'d'"
#
# _______ lo___
# print(lo___.setlocale lo___.LC_NUMERIC, 'Russian_Russia.1251'
# # 'Russian_Russia.1251'
# print(" 0 n ".f...(100000000).re.. "\uffa0", " "
# # 100 000 000
#
# _______ lo___
# print(lo___.setlocale(lo___.LC_NUMERIC, "Russian_Russia.1251"))
# # 'Russian_Russia.1251'
# print(print(lo___.f...("_@", 100000000, grouping _ T...
# # 100 000 000
# print(lo___.localeconv()["thousands_sep"])
# # '\xa0'
#
# print(" 0 ,? ".f... 100000000
# # 100,000,000
#
# print("' @ ? ' ' @ ? ' ' @ #? '".f... 511  # digit | восьмеричное значение:
# # "'511' '777' '0o777'"
#
# print("' @ ? ' ' @ #? '".f... 255    # шестнадцатеричное значение в нижнем регистре:
# # "'ff' '0xff'"
#
# print("' @ ? ' ' @ #? '".f... 255   # шестнадцатеричное значение в верхнем регистре:
# # "'FF' '0XFF'"
#
# print("' 0 @ ' ' 1 @ ' ' 2 @ '".f... 30, 18.6578145, -2.5  # вещественное число в десятичном представлении:
# # "'30.000000' '18.657815' '-2.500000'"
#
# print("' @ .7? ' ' @ .2? '".f... 18.6578145, -2.5     # вещественное число в десятичном представлении:
# # "'18.6578145' '-2.50'"
#
# print("' @ ? ' ' @ ? '".f... 3000, 18657.81452    # вещественное число в экспоненциальной форме (буква в нижнем регистре):
# # "'3.000000e+03' '1.865781e+04'"
#
# print("' @ ? ' ' @ ? '".f... 3000, 18657.81452    # - вещественное число в экспоненциальной форме (буква в верхнем регистре):
# # "'3.000000E+03' '1.865781E+04'"
#
# print("' @ .2? ' ' @ .2? '".f... 3000, 18657.81452    # combination od registers
# # "'3.00e+03' '1.87E+04'"
#
# print("' @ ? ' ' @ ? '".f... 0.086578, 0.000086578     # - эквивалентно f или е (выбирается более короткая запись числа):
# # "'0.086578' '8.6578e-05'"
#
# print("' @ ? ' ' @ ? '".f... 0.086578, 0.000086578    # эквивалентно f или е (выбирается более короткая запись числа):
# # "'0.086578' '8.6578E-05'"
#
"""
% -
"""
# - умножает число на 100 и добавляет символ процента в конец. Значение отображается в соответствии с опцией f.
# print("' @ ? ' ' @ .4? '".f... 0.086578, 0.000086578
# # "'8.657800%' '0.0087%'"
