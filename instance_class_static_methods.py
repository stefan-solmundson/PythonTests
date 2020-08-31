'''
Instance, Class, Static Methods

- static classes don't exist in Python

- instance method = normal
- static method = @staticmethod
- class method = @classmethod
   class methods have a very specific use case as alternate constructors for a class (see below)
   remember that classes are objects too
'''

from datetime import date


class MyClass:
    def method(self):
        return 'instance method called', self

    @staticmethod
    def static_method():
        return 'static method called'

    @classmethod
    def class_method(cls):
        return 'class method called', cls


my_obj = MyClass()
print("Instance Method")
print(my_obj.method())
print("Static Method")
print(my_obj.static_method())
print("Class Method")
print(my_obj.class_method())
print()

#
#
#
# --- Class Methods


class Person:
    standard_age = 11

    def __init__(self, name, age):
        self.name = name
        self.age = age

        # a class method to create a Person object by birth year.

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def is_adult(age):
        return age > 18

    @classmethod
    def print_standard_age(cls):
        print(cls.standard_age)

    @classmethod
    def return_standard_age(cls):
        return cls.standard_age

    @classmethod
    def print_standard_age_add_1(cls):
        cls.standard_age += 1
        print("added 1 to standard age")


person1 = Person('Bob', 21)
person2 = Person.from_birth_year('Bob', 1996)

print("1-1. instance .age attribute")
print(person1.age)
print(person2.age)
print()

print("1-2. @staticmethod is_adult")
print(Person.is_adult(21))
print(person1.is_adult(21))
print(person2.is_adult(21))
print()

print("2-1. print_standard_age")
person1.print_standard_age()
person2.print_standard_age()
person1.print_standard_age_add_1()
person1.print_standard_age()
person2.print_standard_age()
print()

print("2-2. return standard_age")
print(person2.return_standard_age())
print(person1.return_standard_age())
person2.print_standard_age_add_1()
print(person2.return_standard_age())
print(person1.return_standard_age())
print()

print("2-3. Person.standard_age")
print(Person.standard_age)
print(Person.standard_age)
person1.print_standard_age_add_1()
print(Person.standard_age)
print(Person.standard_age)
print()

#
#
#
# ---


# class UniqueIdentifier(object):
#
#     value = 0
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def produce(cls):
#         instance = cls(cls.value)
#         cls.value += 1
#         return instance
#
#
# class FunkyUniqueIdentifier(UniqueIdentifier):
#
#     @classmethod
#     def produce(cls):
#         instance = super(FunkyUniqueIdentifier, cls).produce()
#         instance.name = "Funky %s" % instance.name
#         return instance
#
#
# x = UniqueIdentifier.produce()
# xt = UniqueIdentifier.produce()
# y = FunkyUniqueIdentifier.produce()
# y2 = FunkyUniqueIdentifier.produce()
# yt = FunkyUniqueIdentifier.produce()
# print(x.name)
# print(xt.name)
# print(y.name)
# print(y2.name)
# print(yt.name)
# print(y2.name)
# print(y2.name)

