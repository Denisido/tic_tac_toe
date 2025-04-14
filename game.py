# game.py

from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def main():
    game = Board()
    # Смена игрока.
    current_player = 'X'
    # Флаговая переменная.
    running = True
    game.display()

    while running:
        print(f'Ход делает игрок {current_player}')

        # Запускается бесконечный цикл.
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                if isinstance(row, str):
                    raise ValueError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print(
                    """
                    Пожалуйста, введите значения
                    для строки и столбца заново.
                    """
                )
                continue
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print(
                    '''
                    Пожалуйста, введите значения
                    для строки и столбца заново.
                    '''
                )
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        game.make_move(row, column, current_player)
        print('Ход сделан!')
        game.display()
        if game.check_win(current_player):
            print(f'Победил {current_player}')
            running = False

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
