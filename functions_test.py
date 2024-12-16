import unittest
import functions


class MyTestCase(unittest.TestCase):
    def test_is_number(self):
        self.assertTrue(functions.is_number(5))
        self.assertTrue(functions.is_number(5.5))
        self.assertFalse(functions.is_number("5"))
        self.assertFalse(functions.is_number("5.5"))
        self.assertFalse(functions.is_number("five"))

    def test_is_positive(self):
        self.assertTrue(functions.is_positive(5))
        self.assertTrue(functions.is_positive(5.5))
        self.assertFalse(functions.is_positive(-5))
        self.assertFalse(functions.is_positive(-5.5))


    def test_is_even(self):
        self.assertTrue(functions.is_even(4))
        self.assertTrue(functions.is_even(4.0))
        self.assertFalse(functions.is_even(5))
        self.assertFalse(functions.is_even(5.0))

    def test_is_odd(self):
        self.assertTrue(functions.is_odd(5))
        self.assertTrue(functions.is_odd(5.0))
        self.assertFalse(functions.is_odd(4))
        self.assertFalse(functions.is_odd(4.0))

    def test_is_prime(self):
        self.assertTrue(functions.is_prime(2))
        self.assertTrue(functions.is_prime(3))
        self.assertTrue(functions.is_prime(5))
        self.assertTrue(functions.is_prime(7))
        self.assertTrue(functions.is_prime(11))
        self.assertTrue(functions.is_prime(13))
        self.assertTrue(functions.is_prime(17))
        self.assertTrue(functions.is_prime(19))
        self.assertTrue(functions.is_prime(23))
        self.assertTrue(functions.is_prime(29))
        self.assertTrue(functions.is_prime(31))
        self.assertTrue(functions.is_prime(37))
        self.assertTrue(functions.is_prime(41))
        self.assertTrue(functions.is_prime(43))
        self.assertTrue(functions.is_prime(47))
        self.assertTrue(functions.is_prime(53))
        self.assertTrue(functions.is_prime(59))
        self.assertTrue(functions.is_prime(61))
        self.assertTrue(functions.is_prime(67))
        self.assertTrue(functions.is_prime(71))
        self.assertTrue(functions.is_prime(73))
        self.assertTrue(functions.is_prime(79))
        self.assertTrue(functions.is_prime(83))
        self.assertTrue(functions.is_prime(89))
        self.assertTrue(functions.is_prime(97))
        self.assertFalse(functions.is_prime(1))
        self.assertFalse(functions.is_prime(4))
        self.assertFalse(functions.is_prime(6))
        self.assertFalse(functions.is_prime(8))
        self.assertFalse(functions.is_prime(9))
        self.assertFalse(functions.is_prime(10))
        self.assertFalse(functions.is_prime(12))
        self.assertFalse(functions.is_prime(14))
        self.assertFalse(functions.is_prime(15))
        self.assertFalse(functions.is_prime(16))
        self.assertFalse(functions.is_prime(18))
        self.assertFalse(functions.is_prime(20))
        self.assertFalse(functions.is_prime(21))
        self.assertFalse(functions.is_prime(22))
        self.assertFalse(functions.is_prime(24))
        self.assertFalse(functions.is_prime(25))
        self.assertFalse(functions.is_prime(26))
        self.assertFalse(functions.is_prime(27))
        self.assertFalse(functions.is_prime(28))
        self.assertFalse(functions.is_prime(30))
        self.assertFalse(functions.is_prime(32))
        self.assertFalse(functions.is_prime(33))
        self.assertFalse(functions.is_prime(34))
        self.assertFalse(functions.is_prime(35))
        self.assertFalse(functions.is_prime(36))

    def test_add(self):
        self.assertEqual(functions.add(5, 5), 10)
        self.assertEqual(functions.add(5.5, 5.5), 11)
        self.assertEqual(functions.add(5, 5.5), 10.5)
        self.assertEqual(functions.add(5.5, 5), 10.5)
        self.assertEqual(functions.add("5", 5), "Invalid input")
        self.assertEqual(functions.add(5, "5"), "Invalid input")
        self.assertEqual(functions.add("5", "5"), "Invalid input")
        self.assertEqual(functions.add("five", 5), "Invalid input")
        self.assertEqual(functions.add(5, "five"), "Invalid input")
        self.assertEqual(functions.add("five", "five"), "Invalid input")

    def test_subtract(self):
        self.assertEqual(functions.subtract(5, 5), 0)
        self.assertEqual(functions.subtract(5.5, 5.5), 0)
        self.assertEqual(functions.subtract(5, 5.5), -0.5)
        self.assertEqual(functions.subtract(5.5, 5), 0.5)
        self.assertEqual(functions.subtract("5", 5), "Invalid input")
        self.assertEqual(functions.subtract(5, "5"), "Invalid input")
        self.assertEqual(functions.subtract("5", "5"), "Invalid input")
        self.assertEqual(functions.subtract("five", 5), "Invalid input")
        self.assertEqual(functions.subtract(5, "five"), "Invalid input")
        self.assertEqual(functions.subtract("five", "five"), "Invalid input")

    def test_multiply(self):
        self.assertEqual(functions.multiply(5, 5), 25)
        self.assertEqual(functions.multiply(5.5, 5.5), 30.25)
        self.assertEqual(functions.multiply(5, 5.5), 27.5)
        self.assertEqual(functions.multiply(5.5, 5), 27.5)
        self.assertEqual(functions.multiply("5", 5), "Invalid input")
        self.assertEqual(functions.multiply(5, "5"), "Invalid input")
        self.assertEqual(functions.multiply("5", "5"), "Invalid input")
        self.assertEqual(functions.multiply("five", 5), "Invalid input")
        self.assertEqual(functions.multiply(5, "five"), "Invalid input")
        self.assertEqual(functions.multiply("five", "five"), "Invalid input")

    def test_divide(self):
        self.assertEqual(functions.divide(5, 5), 1)
        self.assertEqual(functions.divide(5.5, 5.5), 1)
        self.assertEqual(functions.divide(5, 5.5), 0.9090909090909091)
        self.assertEqual(functions.divide(5.5, 5), 1.1)
        self.assertEqual(functions.divide("5", 5), "Invalid input")
        self.assertEqual(functions.divide(5, "5"), "Invalid input")
        self.assertEqual(functions.divide("5", "5"), "Invalid input")
        self.assertEqual(functions.divide("five", 5), "Invalid input")
        self.assertEqual(functions.divide(5, "five"), "Invalid input")
        self.assertEqual(functions.divide("five", "five"), "Invalid input")
        self.assertEqual(functions.divide(5, 0), "Division by zero")
        self.assertEqual(functions.divide(5.5, 0), "Division by zero")
        self.assertEqual(functions.divide("5", 0), "Invalid input")
        self.assertEqual(functions.divide("5.5", 0), "Invalid input")
        self.assertEqual(functions.divide("five", 0), "Invalid input")
        self.assertEqual(functions.divide("five", 0), "Invalid input")
        self.assertEqual(functions.divide(0, 5), "Division by zero")
        self.assertEqual(functions.divide(0, 5.5), "Division by zero")
        self.assertEqual(functions.divide(0, "5"), "Invalid input")
        self.assertEqual(functions.divide(0, "5.5"), "Invalid input")
        self.assertEqual(functions.divide(0, "five"),   "Invalid input")
        self.assertEqual(functions.divide(0, "five"), "Invalid input")

    def test_power(self):
        self.assertEqual(functions.power(5, 5), 3125)
        self.assertEqual(functions.power(5.5, 5.5), 11803.064820864423)
        self.assertEqual(functions.power(5, 5.5), 6987.712429686842)
        self.assertEqual(functions.power(5.5, 5), 5032.84375)
        self.assertEqual(functions.power("5", 5), "Invalid input")
        self.assertEqual(functions.power(5, "5"), "Invalid input")
        self.assertEqual(functions.power("5", "5"), "Invalid input")
        self.assertEqual(functions.power("five", 5), "Invalid input")
        self.assertEqual(functions.power(5, "five"), "Invalid input")
        self.assertEqual(functions.power("five", "five"), "Invalid input")

    def test_percentage(self):
        self.assertEqual(functions.percentage(5, 5), 0.25)
        self.assertEqual(functions.percentage(5.5, 5.5), 0.3025)
        self.assertEqual(functions.percentage(5, 5.5), 0.275)
        self.assertEqual(functions.percentage(5.5, 5), 0.275)
        self.assertEqual(functions.percentage("5", 5), "Invalid input")
        self.assertEqual(functions.percentage(5, "5"), "Invalid input")
        self.assertEqual(functions.percentage("5", "5"), "Invalid input")
        self.assertEqual(functions.percentage("five", 5), "Invalid input")
        self.assertEqual(functions.percentage(5, "five"), "Invalid input")
        self.assertEqual(functions.percentage("five", "five"), "Invalid input")


if __name__ == '__main__':
    unittest.main()
