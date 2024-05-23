def lookup(obj):
    """Returns a list of available attributes and methods of an object"""
    return dir(obj)

# Testing with various edge cases

# Case 1: Built-in types
print(lookup(1))  # Integer
print(lookup(3.14))  # Float

# Case 2: Empty class instance
class EmptyClass:
    pass

empty_instance = EmptyClass()
print(lookup(empty_instance))

# Case 3: Built-in function and module
print(lookup(print))  # Built-in function
import sys
print(lookup(sys))  # Built-in module

# Case 4: User-defined class and instance
class MyClass:
    def __init__(self):
        self.attr1 = "value"

    def method1(self):
        pass

instance = MyClass()
print(lookup(instance))

# Case 5: Inherited attributes and methods
class ParentClass:
    def parent_method(self):
        pass

class ChildClass(ParentClass):
    def child_method(self):
        pass

child_instance = ChildClass()
print(lookup(child_instance))

# Case 6: Objects with special methods
class SpecialMethodsClass:
    def __init__(self):
        pass

    def __str__(self):
        return "SpecialMethodsClass instance"

special_instance = SpecialMethodsClass()
print(lookup(special_instance))

# Case 7: None
print(lookup(None))

# Case 8: Large object
class LargeClass:
    def __init__(self):
        for i in range(1000):
            setattr(self, f'attr{i}', i)

large_instance = LargeClass()
print(lookup(large_instance))
