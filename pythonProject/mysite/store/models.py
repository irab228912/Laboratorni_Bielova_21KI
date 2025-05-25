from django.db import models
from datetime import datetime

class calculate:
    def __init__(self):
        self.first_name = input("Введіть ім'я: ") or None
        self.last_name = input("Введіть прізвище: ") or None
        self.birth_year = int(input("Введіть дату народження: ") or None)

    def calculate_course(self):
        if self.birth_year == 2008:
            return "1 курс"
        elif self.birth_year == 2007:
            return "2 курс"
        elif self.birth_year == 2006:
            return "3 курс"
        elif self.birth_year == 2005:
            return "4 курс"
        else:
            return None

    def name_list(self):
        return [self.first_name, self.last_name]

# Тестуємо клас
user = calculate()
print(f"Ваш курс: {user.calculate_course()}")
print(f"Ваш список: {user.name_list()}")