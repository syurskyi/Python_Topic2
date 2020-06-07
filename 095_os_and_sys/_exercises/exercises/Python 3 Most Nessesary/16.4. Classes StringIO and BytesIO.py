# # # -*- coding: utf-8 -*-
#
# # Класс stringIO из модуля io позволяет работать со строкой как с файловым объектом. Все
# # операции с этим файловым объектом (будем называть его далее «файл») производятся
# # в оперативной памяти. Формат конструктора класса:
# # StringIO ( [<Начальное значеЮ1е>] [, newline_None])
# # Если первый параметр не указан, то начальным значением будет пустая строка. После создания
# # объекта указатель текущей позиции устанавливается на начало «файла». Объект, возвращаемый
# # конструктором класса, имеет следующие методы:
# # close () - закрывает «файл». Проверить, открыт «файл» или закрыт, позволяет атрибут
# # closed. Атрибут возвращает True, если «файл» был закрыт, и False - в противном случае;
# # + getvalue () - возвращает содержимое «файла» в виде строки:
# # + tell () - возвращает текущую позицию указателя относительно начала «файла»;
# # + see k ( <Смещение> [, <Позиция>] ) - устанавливает указатель в позицию, имеющую смещение
# # <Смещение> относительно позиции <Позиция:>. В параметре <Позиция> могут быть
# # указаны следующие значения:
# #
# # 0- начало «файла» (значение по умолчанюо);
# # • 1 - текущая позици.я указателя;
# # • 2- конец «файла».
# # getvalue () - возвращает содержимое «файла» в виде строки
# # write (<Строка>) - записывает строку в «файл»:
# # writelines (<Последовательность>) - записывает последовательность в «файл»:
# # read( [ <Количество символов>] ) -считывает данные из «файла». Если параметр не указан,
# # то возврашается содержимое «файла» от текущей позиции указателя до конца «файла
# # ». Если в качестве параметра указать число, то за каждый вызов будет возвращаться
# # указанное количество символов. Когда достигается конец «файла», метод возвращает
# # пустую строку.
# # readline ( [ <Количество символов> J) - считывает из «файла» одну строку при каждом вызове.
# # Возвращаемая строка включает символ перевода строки. Исключением является последняя строка - если она
# # не завершается символом перевода строки, то символ перевода
# # строки добавлен не будет. При достижении конuа «файла» возвращается пустая строка.
# # Если в необязательном параметре указано число, то считывание будет выполняться до тех пор, пока не встретится
# # символ новой строки (\n), символ конца «файла» или из «файла» не будет прочитано указанное количество символов.
# # Иными словами, если количество символов в строке меньше значения параметра, то будет считана одна строка,
# # а не указанное количество символов. Если количество символов в строке больше, то возвращается
# # указанное количество символов.
#
# # readlines ( [ <Примерное количество символов> J )
# #
# # считывает все содержимое «файла»
# # в список. Каждый элемент списка будет содержать одну строку, включая символ перевода строки. Искточением является
# # последняя строка - если она не завершается символом перевода строки, то таковой добавлен не будет.
# #
# # Если в необязательном параметре указано число, то считывается указанное количество символов nmoc фрагмент
# # до символа конца строки \n. Затем эта строка разбивается и добавляется построчно в список.
# # _next_ () - считывает одну строку при каждом вызове. При достижении конuа «файла
# # » возбуждается исключение Stopiteration.
# #
# # Благодаря методу _next_ ( ) мы можем перебирать файл построчно с помощью цикла for.
# # Цикл for на каждой итерации будет автоматически вызывать метод next ().
# # f lush () - сбрасывает данные из буфера в «файл»;
# # • truncate ( [ <Количество сиtv1Волов>]) - обрезает «файл» до указанного количества символов.
# #
# # Если параметр не указан, то «файл» обрезается до текущей позиции указателя
# # Описанные ранее методы writable () и seekbe (), вызванные у объекта класса StringIO,
# # всегда возвращают True.
# # Класс StringIO работает только со строками. Чтобы выполнять аналогичные операции с «файлами»,
# # представляющими собой последовательности байтов, следует использовать
# # класс Bytesro из модуля io. Формат конструктора класса:
# # BytesIO ( [ <Начальное значение>])
# # Класс Bytesro поддерживает такие же методы, что и класс StringIO, но в качестве значений методы принимают
# # и возвращают последовательноsти байтов, а не строки.
# #
# # Класс Bytesro поддерживает также метод getbuffer (), который возвращает ссылку на объект memoryview.
# # С помощью этого объекта можно получать и изменять данные по индексу
# # или срезу, преобразовывать данные в список целых чисел (с помощью метода tolist ()) или в последовательность байтов
# # ( с помощью метода tobytes ( ).
#
# ______ _              # Подключаем модуль
# f _ _.S.I("String1\n")
# ?.g.v.        # Получаем содержимое файла
# # 'String1\n'
# ?.cl..             # Закрываем файл
# # ######################################################################################################################
#
# f _ _.S.I("String1\n")
# ?.te..        # Позиция указателя
# # 0
# ?.se.. 0, 2    # Перемещаем указатель в конец файла
# # 8
# ?.te..        # Позиция указателя
# # 8
# ?.se.. 0      # Перемещаем указатель в начало файла
# # 0
# ?.te..        # Позиция указателя
# # 0
# ?.cl..      # Закрываем файл
# # ######################################################################################################################
#
# f _ _.S.I("String1\n")
# ?.se.. 0, 2)       # Перемещаем указатель в конец файла
# # 8
# ?.write("String2\n")  # Записываем строку в файл
# # 8
# ?.g.v.       # Получаем содержимое файла
# # 'String1\nString2\n'
# ?.cl..           # Закрываем файл
# # ######################################################################################################################
#
# f _ _.S.I
# ?.w.l. "String1\n", "String2\n"
# ?.g.v.         # Получаем содержимое файла
# # 'String1\nString2\n'
# ?.cl..           # Закрываем файл
# # ######################################################################################################################
#
# f _ _.S.I("String1\nString2\n")
# ?.r..()
# # 'String1\nString2\n'
# ?.se.. 0  # Перемещаем указатель в начало файла
# # 0
# ?.r..(5), ?.r..(5), ?.r..(5), ?.r..(5), ?.r..(5)
# # ('Strin', 'g1\nSt', 'ring2', '\n', '')
# ?.cl.. # Закрываем файл
# # ######################################################################################################################
#
# f _ _.S.I("String1\nString2")
# ?.r..l..(), ?.r..l..(), ?.r..l..()
# # ('String1\n', 'String2', '')
# ?.cl.. # Закрываем файл
# # ######################################################################################################################
#
# f _ _.S.I("String1\nString2\nString3\n")
# ?.r..l..(5), ?.r..l..(5)
# # ('Strin', 'g1\n')
# ?.r..l..(100)  # Возвращается одна строка, а не 100 символов
# # 'String2\n'
# ?.cl..      # Закрываем файл
# # ######################################################################################################################
#
# f _ _.S.I("String1\nString2\nString3")
# ?.r..l..s
# # ['String1\n', 'String2\n', 'String3']
# ?.cl.. # Закрываем файл
# # ######################################################################################################################
#
# f _ _.S.I("String1\nString2\nString3")
# ?.r..l..s 14
# # ['String1\n', 'String2\n']
# ?.se.. 0  # Перемещаем указатель в начало файла
# # 0
# ?.r..l..s 17
# # ['String1\n', 'String2\n', 'String3']
# ?.cl.. # Закрываем файл
# # ######################################################################################################################
#
# f _ _.S.I("String1\nString2")
# ?. -n ?. -n
# # ('String1\n', 'String2')
# ?. -n
# # ... Фрагмент опущен ...
# # StopIteration
# ?.cl.. # Закрываем файл
# # ######################################################################################################################
#
# f _ _.S.I("String1\nString2")
# __ line i_ ?
#     print ?.rst..
#
# # String1
# # String2
# ?.cl.. # Закрываем файл
# # ######################################################################################################################
#
# f _ _.S.I("String1\nString2\nString3")
# ?.tru... 15     # Обрезаем файл
# # 15
# ?.g.v.       # Получаем содержимое файла
# # 'String1\nString2'
# ?.cl..         # Закрываем файл
# # ######################################################################################################################
#
# f _ _.S.I("String1\nString2\nString3")
# ?.se.. 15         # Перемещаем указатель
# # 15
# ?.tru...      # Обрезаем файл до указателя
# # 15
# ?.g.v.      # Получаем содержимое файла
# # 'String1\nString2'
# ?.cl..         # Закрываем файл
# # ######################################################################################################################
#
# _______ _             # Подключаем модуль
# f _ _.B.I. _"String1\n"
# ?.se.. 0, 2          # Перемещаем указатель в конец файла
# # 8
# ?.w.. _"String2\n")  # Пишем в файл
# # 8
# ?.g.v.          # Получаем содержимое файла
# # b'String1\nString2\n'
# ?.se.. 0             # Перемещаем указатель в начало файла
# # 0
# ?.r..              # Считываем данные
# # b'String1\nString2\n'
# ?.cl..            # Закрываем файл
# # ######################################################################################################################
#
# f _ _.B.I. _"Python"
# buf _ ?.g.b..
# ? 0                # Получаем значение по индексу
# # b'P'
# ? 0 _ _"J"         # Изменяем значение по индексу
# ?.g.v.          # Получаем содержимое
# # b'Jython'
# ?.t.li.          # Преобразуем в список чисел
# # [74, 121, 116, 104, 111, 110]
# ?.t.by..         # Преобразуем в тип bytes
# # b'Jython'
# ?.cl..            # Закрываем файл
# # ######################################################################################################################