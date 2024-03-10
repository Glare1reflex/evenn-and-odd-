while True:
    number = input("Введите число: ")

    # Проверка на пустой ввод
    if not number.strip():
        print("Вы не ввели число. Попробуйте еще раз.")
        continue

    # Проверка на корректность числа
    try:
        number = int(number)
    except ValueError:
        print("Вы ввели не число. Попробуйте еще раз.")
        continue

    # Анализ четности числа и вывод результата
    if number % 2 == 0:
        print(f"Число {number} является четным.")
    else:
        print(f"Число {number} является нечетным.")

    # Предложение пользователю ввести новое число или выход из программы
    next_action = input("Хотите ввести еще одно число? (да/нет): ").strip().lower()
    if next_action != "да":
        print("Программа завершена.")
        break