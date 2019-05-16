def coffin_price(wood, size):
    _price = 0
    print(wood)
    if wood == 'O':
        _price = 1300
    elif wood == 'B':
        _price = 900
    elif wood == 'P':
        _price == 650
    if size == 'A':
        _price *= 2
    return _price


def flowers_price(size, count):
    if size == 'S':
        _price = 160
    elif size == 'M':
        _price = 450
    elif size == 'B':
        _price = 600
    _price *= count
    return _price


def music_price(typ):
    if typ == 'O':
        _price = 200
    elif typ == 'T':
        _price = 200
    return _price


def labour_price():
    _price = 0
    labour = {'transport': 380,
              'prepare_body': 600,
              'funeral_service': 580,
              'fees_grave': 80,
              'freezer': 210}
    for price in labour.values():
        _price += price
    return _price
