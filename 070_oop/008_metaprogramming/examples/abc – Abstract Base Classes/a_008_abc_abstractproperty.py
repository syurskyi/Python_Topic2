# abc_abstractproperty.py

# Abstract Properties
# If an API specification includes attributes in addition to methods, it can require the attributes in concrete classes
# by combining abstractmethod() with property().


import abc


class Base(abc.ABC):

    @property
    @abc.abstractmethod
    def value(self):
        return 'Should never reach here'

    @property
    @abc.abstractmethod
    def constant(self):
        return 'Should never reach here'


class Implementation(Base):

    @property
    def value(self):
        return 'concrete property'

    constant = 'set by a class attribute'


try:
    b = Base()
    print('Base.value:', b.value)
except Exception as err:
    print('ERROR:', str(err))

i = Implementation()
print('Implementation.value   :', i.value)
print('Implementation.constant:', i.constant)


# The Base class in the example cannot be instantiated because it has only an abstract version of the property getter
# methods for value and constant. The value property is given a concrete getter in Implementation and constant is
# defined using a class attribute.

# $ python3 abc_abstractproperty.py
#
# ERROR: Can't instantiate abstract class Base with abstract
# methods constant, value
# Implementation.value   : concrete property
# Implementation.constant: set by a class attribute

# # python 2
#
# # import abc
# #
# # class Base(object):
# #     __metaclass__ = abc.ABCMeta
# #
# #     @abc.abstractproperty
# #     def value(self):
# #         return 'Should never get here'
# #
# #
# # class Implementation(Base):
# #
# #     @property
# #     def value(self):
# #         return 'concrete property'
# #
# #
# # try:
# #     b = Base()
# #     print 'Base.value:', b.value
# # except Exception, err:
# #     print 'ERROR:', str(err)
# #
# # i = Implementation()
