# задание 1
class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0, 0],
                [0, 0],
                [0, 0]]

        for i in range(len(self.list_1)):
            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

matrix = Matrix([[31, 32],
                    [37, 43],
                    [41, 86]],
                   [[22, 15],
                    [16, 12],
                    [37, 36]])

print(matrix.__add__())

# задание 2
class Project:
    def __init__(self, V, H):
        self.V = V
        self.H = H

    def square_c(self):
        return self.V / 6.5 + 0.5

    def square_s(self):
        return self.H * 2 + 0.3

    @property
    def square(self):
        return str(f'Площадь общая ткани \n'
                   f' {(self.V / 6.5 + 0.5) + (self.H * 2 + 0.3)}')
class Coat(Project):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.square_c = round(self.V / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.square_c}'
class Suit(Project):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.square_s = round(self.H * 2 + 0.3)

    def __str__(self):
        return f'Площадь на пальто {self.square_s}'
coat = Coat(10, 0)
suit = Suit(0, 5)
print(coat)
print(suit)

# задание 3
class Cell:
    def __init__(self, cells):
        self.cells = int(cells)

    def __str__(self):
        return f'{self.cells * "*"}'

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        return Cell(int(self.cells - other.cells))

    def __mul__(self, other):
        return Cell(int(self.cells * other.cells))

    def __truediv__(self, other):
        return Cell(round(self.cells // other.cells))

    def make_order(self, cells_new):
        row = ''
        for i in range(int(self.cells / cells_new)):
            row += f'{"*" * cells_new} \\n'
        row += f'{"*" * (self.cells % cells_new)}'
        return row

cells1 = Cell(15)
cells2 = Cell(8)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(3))
print(cells1.make_order(1))
print(cells1 / cells2)

