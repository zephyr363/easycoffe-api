from injector import Module, singleton, noscope, Binder
from dao import *


class AppModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(CoffeeDAO, to=CoffeeDAO, scope=singleton)
        binder.bind(UserDAO, to=UserDAO, scope=singleton)
        binder.bind(ProfileDAO, to=ProfileDAO, scope=singleton)
        binder.bind(CoffeeCategoryDAO, to=CoffeeCategoryDAO, scope=singleton)
