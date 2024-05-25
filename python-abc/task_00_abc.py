#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"


if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    print(f"Dog sound: {dog.sound()}")  # Output: Dog sound: Bark
    print(f"Cat sound: {cat.sound()}")  # Output: Cat sound: Meow
