def is_table_free(num):
    return tables[num] is None


def delete_reservation(num):
    tables[num] = None


def reserve_table(num, name, is_vip):
    if tables[num] is None:
        tables[num] = {'name': name, 'is_vip': is_vip}


tables = {
    1: {'name': 'Andrey', 'is_vip': True},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False},
    6: None,
    7: None,
    8: None,
    9: None,
}

print(tables)
reserve_table(3, 'Gena', True)
reserve_table(4, 'Artem', False)
reserve_table(5, 'Artur', True)  # Артур не должен занять место Василия
print(tables)

'''
{1: {'name': 'Andrey', 'is_vip': True}, 2: None, 3: 'Gena', 4: 'Artem', 5: {'name': 'Vasiliy', 'is_vip': False}, 6: None, 7: None, 8: None, 9: None, 'is_vip': False}'''
