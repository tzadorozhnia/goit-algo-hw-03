from datetime import datetime

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

print(get_days_from_today("2025-09-20"))