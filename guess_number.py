"""Игра «Угадай число» (бинарный поиск).

Функция:
    guess_binary(target, low, high) -> (number, attempts)

Она ищет загаданное целое число в границах [low, high]
и возвращает пару (найденное_число, количество_попыток).
"""


def guess_binary(target: int, low: int, high: int) -> tuple[int, int]:
    """Ищет число с помощью бинарного поиска.

    Аргументы:
        target: какое число нужно найти.
        low: нижняя граница (включительно).
        high: верхняя граница (включительно).

    Возврат:
        (number, attempts) — найденное число и сколько попыток было.

    Ошибки:
        TypeError — если target/low/high не целые числа (int).
        ValueError — если границы неверные или target вне [low, high].
    """
    # Проверка типов (просто и понятно)
    if not isinstance(target, int) or not isinstance(low, int) or not isinstance(high, int):
        raise TypeError("target, low, high должны быть целыми числами (int).")

    # Проверка границ
    if low > high:
        raise ValueError("low должен быть меньше или равен high.")
    if target < low or target > high:
        raise ValueError("target должен быть внутри [low, high].")

    attempts = 0
    lo = low
    hi = high

    # Классический бинарный поиск
    while lo <= hi:
        mid = (lo + hi) // 2
        attempts += 1

        if mid == target:
            return mid, attempts
        elif mid < target:
            lo = mid + 1
        else:
            hi = mid - 1

    # Сюда не дойдём при правильных входных данных.
    raise RuntimeError("Число не найдено из-за внутренней ошибки.")


if __name__ == "__main__":
    # Простой запуск через ввод пользователя
    print("Игра «Угадай число» — бинарный поиск")
    print("Пример: low=1, high=100, target=42\n")
    try:
        low = int(input("Введите low: "))
        high = int(input("Введите high: "))
        target = int(input("Введите target (между low и high): "))

        number, attempts = guess_binary(target, low, high)
        print(f"\nНайдено! Число: {number}. Попыток: {attempts}.")
    except Exception as e:
        print("Ошибка:", e)
