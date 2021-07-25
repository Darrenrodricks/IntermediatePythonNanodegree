# class BaseClass():
#     def simple_method():
#         return 'hello'
#
# class SimpleClass(BaseClass):
#     def simple_method():
#         return super().simple_method() + ' world'
#
# class FoodInterface(ABC):
#     ...
#     cooking_temp = 200
#     def __init__(self, isVegan):
#         self.isVegan = isVegan
#
#     @abstractmethod
#     def eat(self):
#         pass
#
#     @classmethod
#     def cook(cls, isVegan):
#         if temp > cls.cooking_temp:
#             return cls(isVegan)
#
# class HotDog(FoodInterface):
#
#     def eat(self):
#         print('bite')
#
#     def applyCondiments(self, type):
#         self.condiments.append(type)