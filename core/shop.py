from core.cargo import Cargo
from core.storage import Storage


class Shop(Storage):

    def __init__(self, batch_of_goods, capacity=100):
        super().__init__(batch_of_goods, capacity)

    @property
    def title(self):
        return 'Магазин'

    def add(self, cargo: Cargo):
        items = self.get_items()

        if cargo.name in items or len(items) < 5:
            return self._add_cargo(cargo)

        return False

    def remove(self, cargo: Cargo) -> bool:
        return self._remove_cargo(cargo)
