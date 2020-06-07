﻿# Задание другого имени при импортировании

import fibonacci as fib

print(fib.nth_fibonacci(10))  # теперь модуль доступен под именем fib
print(fib.__name__)  # но это лишь идентификатор в текущем модуле, а реальное имя не изменилось