import json

from core.cargo import Cargo
from core.storage import Storage


class Store(Storage):

    def __init__(self, batch_of_goods, capacity=100):
        super().__init__(batch_of_goods, capacity)

    @property
    def title(self):
        return 'Склад'

    def add(self, cargo: Cargo):
        return self._add_cargo(cargo)

    def remove(self, cargo: Cargo) -> bool:
        return self._remove_cargo(cargo)
