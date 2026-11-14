def binomial(n,k):
    if n == k or k == 0:
        return 1
    else:
        return binomial(n - 1, k - 1) + binomial(n - 1, k)

cases = [
    (0, 0, 1), (1, 0, 1), (1, 1, 1),
    (5, 0, 1), (5, 5, 1), (5, 2, 10),
    (6, 3, 20), (7, 2, 21), (7, 5, 21), (10, 5, 252),
]

for n, k, expected in cases:
    assert binomial(n, k) == expected, f'Помилка для n={n}, k={k}'
print('Усі перевірки завдання 3 пройдено!')