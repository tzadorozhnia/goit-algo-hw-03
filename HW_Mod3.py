from datetime import datetime
import random

def get_days_from_today(date: str) -> int | str:
    """
        Функція обчислює кількість днів між заданою датою та поточною датою.

        :param date: рядок у форматі 'YYYY-MM-DD'
        :return: ціле число (може бути від'ємним), що вказує різницю у днях
        """
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        return given_date.toordinal() - today.toordinal()
    except ValueError:
        return f"Помилка: '{date}' не відповідає формату 'YYYY-MM-DD'."


def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> list[int]:
    """
    Функція повертає випадковий набір чисел у межах заданих параметрів.

    :param min_value: мінімальне можливе число у наборі (не менше 1)
    :param max_value: максимальне можливе число у наборі (не більше 1000)
    :param quantity: кількість чисел, які потрібно вибрати (значення між min і max)
    :return: список цілих чисел, відсортований без повторів, або порожній список при некоректних параметрах
    """

    if min_value < 1:
        return []
    if max_value > 1000:
        return []
    if quantity > (max_value - min_value + 1):
        return []

    res = random.sample(range(min_value, max_value + 1), quantity)
    res.sort()
    return res
