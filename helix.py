n = int(input())

# Создаем квадратную матрицу, заполненную нулями.
helix = [[0] * n for i in range(n)]

# Счетчики для заполнения цикла.
b = 0    # Якорь который, увеличивается после прохода 4 циклов заполнения спирали
c = 1    # Текущее значение ячейки матрицы
if n == 1:
    helix[0][0] = 1
else:
    while b < n // 2:
        m = n - b * 2 - 1    # Задаем диапозон, в котором будет происходит каждый цикл
        for x in range(m):
            helix[b][b + x] = c
            c += 1
        for y in range(m):
            helix[b + y][n - 1 - b] = c
            c += 1
        for x in range(m):
            helix[n - 1 - b][n - 1 - b - x] = c
            c += 1
        for y in range(m):
            helix[n - 1 - y - b][b] = c
            c += 1
        b += 1
        if n % 2:
            helix[b][b] = c

for y in helix:    # Выводим готовую спираль
    print(*y, end=' ')
    print()
