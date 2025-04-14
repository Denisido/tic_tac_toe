class FieldIndexError(IndexError):
    """
    Выбрасывается, если выбрано значение вне поля
    """

    def __init__(self,
                 #  Тут текст по умолчанию.
                 message='Введено значение по умолчанию!!!'):
        super().__init__(message)


class CellOccupiedError(Exception):
    def __init__(self,
                 message='Попытка изменить занятую ячейку...'):
        super().__init__(message)
