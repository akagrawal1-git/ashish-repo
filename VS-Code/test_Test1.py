import unittest

from Test1 import nth_prime


class TestNthPrime(unittest.TestCase):
    def test_small_primes(self):
        cases = [
            (1, 2),
            (2, 3),
            (3, 5),
            (4, 7),
            (5, 11),
            (6, 13),
            (10, 29),
        ]
        for n, expected in cases:
            with self.subTest(n=n):
                self.assertEqual(nth_prime(n), expected)

    def test_larger_primes(self):
        cases = [
            (100, 541),
            (1000, 7919),
        ]
        for n, expected in cases:
            with self.subTest(n=n):
                self.assertEqual(nth_prime(n), expected)

    def test_invalid_inputs(self):
        for bad in (0, -1, -10):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    nth_prime(bad)

    def test_repeatability(self):
        # calling twice should give the same result
        self.assertEqual(nth_prime(100), nth_prime(100))


if __name__ == "__main__":
    unittest.main()
