import re

def normalize_phone(phone_number: str) -> str:
    """
    Нормалізує телефонний номер до формату +380XXXXXXXXX

    :param phone_number: рядок з номером у довільному форматі
    :return: нормалізований номер (рядок)
    """
    # Забираємо пробіли на початку/кінці
    phone_number = phone_number.strip()

    # Видаляємо всі символи, крім цифр та '+'
    phone_number = re.sub(r"[^\d+]", "", phone_number)

    # Якщо номер починається з '+38...' — все ок
    if phone_number.startswith("+38"):
        return phone_number

    # Якщо починається з '380...' — додаємо '+'
    elif phone_number.startswith("380"):
        return "+" + phone_number

    # Якщо починається з '0...' — додаємо '+38'
    elif phone_number.startswith("0"):
        return "+38" + phone_number

    # Якщо починається з інших цифр — підстрахуємо і додамо '+'
    else:
        return "+" + phone_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)