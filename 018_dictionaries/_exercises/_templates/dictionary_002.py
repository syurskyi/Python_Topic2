# # -*- coding: utf-8 -*-
#
# # Проверить существование кточа можно с помощью оператора i_. Если ключ найден, то
# # возвращается значение тrue, в противном случае - False.
# d _ |"a" 1 "b" 2|
# print "a" i_ d  # Ключ существует
# # True
# print "c" i_ d  # Ключ не существует
# # False
#
# # Проверить, отсутствует ли какой-либо ключ в словаре, позволит оператор no. i_. Если
# # ключ отсутствует, возвращается True, иначе - False.
# d _ |"a" 1, "b" 2|
# print "c" no. i_ d  # Ключ не существует
# # True
# print "a" no. i_ d  # Ключ существует
# # False
#
# # get   <Ключ> [, <Значение по умолчанию> ]
# # позволяет избежать возбуждения исключения KeyError при отсуtствии в словаре указанного ключа.
# # Если ключ присутствует в словаре, то метод возвращает значение, соответствующее этому ключу.
# # Если ключ отсутствует, то возвращается None или значение, указанное во втором параметре.
# #
# d _ |"a" 1 "b" 2|
# print d.ge. "a"  d.ge. "c"  d.ge. "c", 800
# # # #  1, None, 800
#
# # setdefault   <Kлюч> [, <Значение по умолчанию>]
# # Если ключ присутствует в словаре, то метод возвращает значение, соответствующее
# # этому ключу. Если ключ отсутствует, то в словаре создается новый элемент со значением, указанным во втором параметре.
# # Если второй параметр не указан, значением нового элемента будет None.
# #
# d _ |"a" 1, "b" 2|
# print d.s.. "a"  d.s... "c"  d.s... "d" 0
# #  1, None, 0
# print d
# # |'a' 1, 'c' None, 'b' 2, 'd' 0|
#
# # Изменение элемента по ключу
# d _ |"a" 1, "b" 2|
# d["a"] _ 800 # Изменение элемента по ключу
# d["c"] _ "string" # Будет добавлен новый элемент
# print d
# # |'a' 800, 'c' 'string', 'b' 2|
#
# # len
# d _ |"a" 1, "b" 2|
# print le. d  # Получаем количество ключей в словаре
# # 2
#
# # del
# d _ |"a" 1, "b" 2|
# del d|"b"|; print d    # Удаляем элемент с ключом "b" и выводим словарь
# # |'a' 1|
#
# # Perebor elementov slovarja
# d _ |"x" 1, "y" 2, "z" 3|
# ___ key i_ d.keys
#     print " |0| _> |1| ".format key, d[key] , end_" "
# # Выведет  y _> 2   x _> 1   z _> 3
#
# ___ key i_ d
#     print " |0| _> |1| ".format key, d[key] , end_" "
# # Выведет  y _> 2   x _> 1   z _> 3
#
# # Получаем список ключей
# d _ |"x" 1, "y" 2, "z" 3|
# k _ list d.keys ))  # Получаем список ключей
# k.sort   # Сортируем список ключей
# ___ key i_ k
#     print " |0| _> |1| ".format key, d[key] , end_" "
# # Выведет  x _> 1   y _> 2   z _> 3
#
# # sorted
# d _ |"x" 1, "y" 2, "z" 3|
# ___ key i_ sorted d.keys ))
#     print " |0| _> |1| ".format key, d[key] , end_" "
# # Выведет  x _> 1   y _> 2   z _> 3
#
# # Так как на каждой итерации возвращается кmоч словаря, функции sorted     можно сразу передать объект словаря,
# # а не результат выполнения метода keys
#
# d _ |"x" 1, "y" 2, "z" 3|
# ___ key i_ so.. d
#     print " |0| _> |1| ".f... k.. d|k..|  e.._" "
# # Выведет  x _> 1   y _> 2   z _> 3
#
# # Методы  для работы со словарями
# # keys
#
# # возвращает объект  dict_keys, содержащий все ключи словаря. Этот объект
# # поддерживает итерации, а также операции над множествами
# #
# d1, d2 _ |"a" 1 "b" 2 | |"a" 3 "c" 4 "d" 5|
# print d1.keys  , d2.keys ))  # Получаем объект dict_keys
# #  dict_keys ['a', 'b'] , dict_keys ['a', 'c', 'd']))
# print li.. d1.k... ; li.. d2.k...
#  # Получаем список ключей
# #  ['a', 'b'], ['a', 'c', 'd']
# ___ k i_ d1.k..
#   print k e.._" "
#
# # Методы  для работы со словарями
# # keys    - Объединение
# d1, d2 _ |"a" 1, "b" 2|, |"a" 3, "c" 4, "d" 5|
# print d1.ke..   | d2.ke..
# # |'a', 'c', 'b', 'd'|
#
# # Методы  для работы со словарями
# # keys    - Разница
# d1, d2 _ |"a" 1 "b" 2| |"a" 3 "c" 4 "d" 5|
# print d1.k..   - d2.k..
# # |'b'|
# print d2.ke..   - d1.k...
# # |'c', 'd'|