from core.cargo import Cargo
from core.shop import Shop
from core.store import Store


def print_storages(storages):
    for i in range(len(storages)):
        print(f'[{i + 1}] {storages[i].title} - {storages[i]}')


def print_goods(goods: list[Cargo]):
    for i in range(len(goods)):
        c = goods[i]
        print(f'[{i + 1}] {c.name} - {c.amount}')


DEFAULT_STORE_GOODS = [
    Cargo('Печеньки', 10),
    Cargo('Сосиськи', 10),
    Cargo('Сардельки', 10)
]


def get_source(storages):
    while True:
        source = int(input('Откуда забираем? '))

        if source < 1 or len(storages) < source:
            continue

        source_store = storages[source - 1]

        if source_store.get_unique_items_count() > 0:
            goods = source_store.get_items_cargo()
            return source_store, goods
        else:
            print('Тут ничего нетути...')


def get_good(goods):
    while True:
        print_goods(goods)
        good = int(input('Укажите товар: '))

        if 0 < good <= len(goods):
            return goods[good - 1]


def get_cargo(source_good):
    while True:
        amount = int(input(f'Укажите число: (1-{source_good.amount})'))
        if amount < source_good.amount:
            print('Пакуем товар...')
            return Cargo(source_good.name, amount)
        else:
            print('Не хватает на складе, попробуйте заказать меньше')


def start():
    storages = [Store(DEFAULT_STORE_GOODS), Shop([])]

    while True:
        print('===================')
        print('=== Новый заказ ===')
        print('===================')

        print_storages(storages)

        # Определяем точку отправления
        source_store, goods = get_source(storages)

        # Определяем товар
        source_good = get_good(goods)

        # Формируем посылку
        cargo = get_cargo(source_good)

        # Определяем точку назначения
        while cargo is not None:
            print_storages(storages)
            destination = int(input('Куда перевозим? '))
            destination_store = storages[destination - 1]

            print('Перевозим...')
            if destination_store.add(cargo):
                source_store.remove(cargo)
                cargo = None
                print('Готово!!!')
            else:
                print('В магазин недостаточно места, попобуйте что то другое')
