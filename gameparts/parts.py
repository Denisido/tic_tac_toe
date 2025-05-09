# gameparts/parts.py

class Board:
    """
    Класс, который  описывает игровое поле.
    """

    # Атрибут класса.
    field_size = 3

    # Инициализировать игровое поле - список списков с пробелами.
    # Пробелы - это пустые клетки.
    def __init__(self):
        self.board = [
            [' ' for _ in range(self.field_size)]
            for _ in range(self.field_size)
        ]

    # Метод, который обрабатывает ходы игроков.
    def make_move(self, row, col, player):
        self.board[row][col] = player

    # Метод, который отрисовывает игровое поле.
    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_board_full(self):
        for i in range(self.field_size):
            for j in range(self.field_size):
                if self.board[i][j] == ' ':
                    # game is going on
                    return False
        return True

    def check_win(self, player):
        # Проверка по горизонтали и вертикали.
        for i in range(self.field_size):
            if (
                all([self.board[i][j] ==
                     player for j in range(self.field_size)])
                or
                all([self.board[j][i] ==
                     player for j in range(self.field_size)])
            ):
                return True

        # Проверка по диагонали.
        if (
            all([self.board[i][i] ==
                 player for i in range(self.field_size)])
            or
            all(
                [self.board[i][self.field_size - 1 - i] == player
                    for i in range(self.field_size)])
        ):
            return True

        return False

    # Переопределяем метод __str__
    def __str__(self):
        return (
            'Объект игрового поля размером'
            f'{self.field_size} x {self.field_size}'
        )
