def make_link(value, tail=None):
    return (value, tail)

def sum_links(chain):
    if chain is None:
        return 0
    else:
        return chain[0] + sum_links(chain[1])

assert make_link(5) == (5, None)
assert make_link('кінець', None) == ('кінець', None)
chain = make_link(3, make_link(2, make_link(1)))
assert chain == (3, (2, (1, None)))
assert chain[1][1][0] == 1

tail = make_link(10)
head = make_link(20, tail)
assert head[1] is tail
assert tail == (10, None)
print('Усі перевірки частини 1 пройдено!')

assert sum_links(None) == 0
assert sum_links(make_link(7)) == 7
assert sum_links(make_link(0)) == 0
chain = make_link(3, make_link(2, make_link(1)))
assert sum_links(chain) == 6
assert chain == (3, (2, (1, None))), 'Вхідний ланцюжок змінено'
assert sum_links(make_link(2, make_link(-5, make_link(3)))) == 0
print('Усі перевірки частини 2 пройдено!')