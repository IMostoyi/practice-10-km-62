def recursive_len(items):
    if items == []:
        return 0
    else:
        return 1 + recursive_len(items[1:])
        

for items in ([], [True], [1, 2, 3], [1, 0, 3], ['', 'текст'], [None], [[1], 'так', -2], [True, []]):
    original = items.copy()
    result = recursive_len(items)
    assert result == len(items), f'Помилка для {items!r}'
    assert type(result) is int, 'Результат має бути цілим числом'
    assert items == original, 'Початковий список змінено'
print('Усі перевірки завдання 2 пройдено!')