'''
static classes don't exist in Python
instance methods = normal
static method = @staticmethod
class method = @classmethod
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

#
#
#
# --- Class Methods


class Person:
    age = "11"
    bool_test = 11

    def __init__(self, name, age):
        self.name = name
        self.age = age

        # a class method to create a Person object by birth year.

    @classmethod
    def from_birth_year(cls, name, year):
        bool_test = 22
        age = "22"
        return cls(name, date.today().year - year)

        # a static method to check if a Person is adult or not.

    @staticmethod
    def is_adult(age):
        return age > 18

    @classmethod
    def bool_test(cls):
        return str.format("x is {}", cls.bool_test)

    # @classmethod
    def print_age(cls):
        return cls.age

    def print_age_add_1(cls):
        cls.age += 1
        return "1 added"

    @classmethod
    def print_age2(cls):
        print(cls.age)

    # def print_age(cls):
    #     return cls.age


person1 = Person('Bob', 21)
person2 = Person.from_birth_year('Bob', 1996)

print(person1.age)
print(person2.age)
print(person1.bool_test())
print("f")
print(person2.bool_test())

# --

print(person1.print_age())
print(person2.print_age())

print(person1.print_age_add_1())

print(Person.print_age)

print(person1.print_age())
print(person2.print_age())
# print(Person.print_age(person1))
# print(Person.print_age(person2))

# print the result
# print(Person.is_adult(22))

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

