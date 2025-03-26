import unittest
from prime_number import nth_prime, is_prime 

class TestPrimeFunctions(unittest.TestCase):

    def test_is_prime_positive_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(101))

    def test_is_prime_positive_non_primes(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(100))

    def test_is_prime_negative_numbers(self):
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(-10))

    def test_is_prime_zero(self):
        self.assertFalse(is_prime(0))

    def test_nth_prime_positive_n(self):
        self.assertEqual(nth_prime(1), 2)
        self.assertEqual(nth_prime(2), 3)
        self.assertEqual(nth_prime(3), 5)
        self.assertEqual(nth_prime(6), 13)
        self.assertEqual(nth_prime(10), 29)
        self.assertEqual(nth_prime(10001), 104743)

    def test_nth_prime_zero_or_negative_n(self):
        self.assertIsNone(nth_prime(0))
        self.assertIsNone(nth_prime(-1))
        self.assertIsNone(nth_prime(-10))

if __name__ == '__main__':
    unittest.main()