from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
import aiogram
import pygame



if __name__ == '__main__':
    print("Запуск программы.")
    salary = calculate_salary()
    people = get_employees()

    now = datetime.datetime.now()
    print(f"Текущее время: {now}")
    print("Программа завершена.")

