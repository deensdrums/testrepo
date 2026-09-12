import unittest

from calculator import add


class CalculatorTest(unittest.TestCase):
    def test_positive(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_negative_first(self) -> None:
        self.assertEqual(add(-2, 1), -1)

    def test_both_negative(self) -> None:
        self.assertEqual(add(-2, -3), -5)

    def test_zero(self) -> None:
        self.assertEqual(add(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
