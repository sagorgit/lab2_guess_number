"""Тесты для игры «Угадай число» (бинарный поиск)."""

import math
import unittest
from guess_number import guess_binary


class TestGuessNumberBinary(unittest.TestCase):
    def test_one_value_interval(self):
        # Граница из одного числа: должно найтись за 1 попытку
        self.assertEqual(guess_binary(5, 5, 5), (5, 1))

    def test_low_mid_high_targets(self):
        # Проверяем разные диапазоны и цели: low, середина, high
        cases = [(1, 100), (1, 10), (20, 40), (-50, 50)]
        for low, high in cases:
            mid = (low + high) // 2
            for target in (low, mid, high):
                number, attempts = guess_binary(target, low, high)
                self.assertEqual(number, target)
                # Для бинарного поиска попыток мало: примерно log2(n)
                n = high - low + 1
                self.assertLessEqual(attempts, math.ceil(math.log2(n)) + 1)

    def test_invalid_types(self):
        # Не int -> должна быть ошибка типов
        with self.assertRaises(TypeError):
            guess_binary(5.0, 1, 10)  # type: ignore[arg-type]

    def test_invalid_bounds(self):
        # Неверные границы или цель вне диапазона -> ValueError
        with self.assertRaises(ValueError):
            guess_binary(5, 10, 1)
        with self.assertRaises(ValueError):
            guess_binary(0, 1, 10)


if __name__ == "__main__":
    # Запуск тестов из VS Code / терминала: python test_guess.py
    # (В Google Colab можно так: unittest.main(argv=[''], verbosity=2, exit=False))
    unittest.main(verbosity=2)
