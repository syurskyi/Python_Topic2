import inspect

import example

for name, data in inspect.getmembers(example, inspect.isclass):
    print('{} : {!r}'.format(name, data))

