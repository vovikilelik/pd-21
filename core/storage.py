import json
from abc import ABC, abstractmethod

from core.cargo import Cargo


class Storage(ABC):
    capacity = 0
    batch_of_goods: list[Cargo] = []

    def __init__(self, batch_of_goods, capacity):
        self.batch_of_goods = batch_of_goods
        self.capacity = capacity

    @abstractmethod
    def add(self, cargo: Cargo) -> bool:
        pass

    @abstractmethod
    def remove(self, cargo: Cargo) -> bool:
        pass

    @property
    @abstractmethod
    def title(self):
        pass

    def __remove_cargo(self, cargo: Cargo):
        for item in self.batch_of_goods:
            if item.name == cargo.name:
                if item.amount <= cargo.amount:
                    self.batch_of_goods.remove(item)
                    return Cargo(cargo.name, cargo.amount - item.amount)
                else:
                    item.amount -= cargo.amount
                    return Cargo(cargo.name, 0)

        return False

    def _remove_cargo(self, cargo: Cargo):
        result = cargo
        changed = False

        while result is not False and result.amount > 0:
            result = self.__remove_cargo(result)
            if result is not False:
                changed = True

        return changed

    def _add_cargo(self, cargo: Cargo):
        if self.get_items_count() < self.capacity:
            self.batch_of_goods.append(cargo)
            return True

        return False

    def get_items_count(self):
        count = 0

        for item in self.batch_of_goods:
            count += item.amount

        return count

    def get_items(self):
        store = {}

        for item in self.batch_of_goods:
            if item.name in store:
                store[item.name] += item.amount
            else:
                store[item.name] = item.amount

        return store

    def get_items_cargo(self):
        items = self.get_items()
        return [Cargo(name, amount) for name, amount in items.items()]

    def get_unique_items_count(self):
        store = self.get_items()
        return len(store)

    def __str__(self):
        return json.dumps(self.get_items(), ensure_ascii=False)
