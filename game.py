# game.py

from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def save_result(text):
    # Открыть файл example.txt на чтение (аргумент 'r').
    file = open('results.txt', 'a', encoding='utf-8')
    # Прочитать первые 12 символов из файла и сохранить их в переменную.
    file.write(text)
    file.close()


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
            text = f'Победил {current_player}\r'
            print(text)
            running = False
            save_result(text)

        elif game.is_board_full():
            # Сформировать строку.
            text = 'Ничья!'
            # Вывести строку на печать.
            print(text)
            # Добавить строку в файл.
            save_result(text)
            running = False

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
