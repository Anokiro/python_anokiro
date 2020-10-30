# Урок 7, задача 1.
# Матрицы.
def main():
    class Matrix:
        def __init__(self, matrix):
            self.matrix = matrix

        def __str__(self):
            for i in self.matrix:
                for j in i:
                    print(f'{j:<5}', end='')
                print()
            return ''

        def __add__(self, other):
            list = []
            for i, j in zip(self.matrix, other.matrix):
                sum = (i[0] + j[0]), (i[1] + j[1])
                list.append(sum)

            for el in list:
                for el2 in el:
                    print(f'{el2:<5}', end='')
                print()
            return ''

    matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
    print(matrix_1)

    matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
    print(matrix_2)
    print('---сумма мартиц---')
    print(matrix_1 + matrix_2)


main()
