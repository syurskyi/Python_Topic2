# # Just because our class implements the context manager protocol does not mean it cannot do other things as well!
# # In fact the open function we use to open files can be used with or without a context manager:
#
# print('#' * 52 + '  ### Not Just a Context Manager')
#
# f _ o.. test.txt '_'
# ?.w..l.. 'this is a test'
# ?.c..
#
# # Here we did not use a context manager - the open function simply returned the file object - but we had to close
# # the file ourselves - there was not context used.
# # On the other hand we can also use it with a context manager:
#
# print('#' * 52 + '  On the other hand we can also use it with a context manager:')
#
# w___ o.. test.txt __ f
#     print(?.r.l.
# # ['this is a test']
# # ######################################################################################################################
#
# print('#' * 52 + '  We can implement classes that implement their own functionality'
#                  '  as well as a context manager if we want to.')
#
# # We can implement classes that implement their own functionality as well as a context manager if we want to.
#
# c_ DataIterator:
#     ___ - fname
#         ____._f.. _ ?
#         ____._f _ N..
#
#     ___ -i ____
#         r_ ____
#
#     ___ -n ____
#         row _ n.. ____._f
#         r_ ro_.st.. '\n' .sp.. ','
#
#     ___ -e ____
#         ____._f _ o... ____._fn..
#         r_ ____
#
#     ___ -e
#         __ n.. ____._f.c..
#             ____._f.c..
#         r_ F...
#
#
# w___ D...  'nyc_parking_tickets_extract.csv' __ data
#     ___ row __ ?
#         print ?
#
# print('#' * 52 + '  Of course, we cannot use this iterator without also using the context manager'
#                  '  since the file would not be opened otherwise:')
#
# data _ D... 'nyc_parking_tickets_extract.csv'
#
# # for row in data:
# #     print(row)    # TypeError: 'NoneType' object is not an iterator
# # ######################################################################################################################
#
# # But I want to point out that creating the context manager and using the with statement can be done in two steps
# # if we want to:
# print('#' * 52 + '  But I want to point out that creating the context manager and using the `with` statement'
#                  '  can be done in two steps if we want to:')
#
# data_iter _ D.. 'nyc_parking_tickets_extract.csv'
#
# # At this stage, the object has been created, but the __enter__ method has not been called yet.
# # Once we use with, then the file will be opened, and the iterator will be ready for use:
#
# w... ? __ data
#     ___ row __ ?
#         print ?
#
