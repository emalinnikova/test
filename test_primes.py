"""Tests for the inclusive prime sieve and prime-counting function."""

import unittest

from primes import prime_count, sieve


class PrimeTests(unittest.TestCase):
    def test_limits_below_two(self):
        for limit in (-100, -1, 0, 1):
            with self.subTest(limit=limit):
                self.assertEqual(sieve(limit), [])
                self.assertEqual(prime_count(limit), 0)

    def test_small_values_and_inclusive_boundaries(self):
        cases = {
            2: [2],
            3: [2, 3],
            4: [2, 3],
            10: [2, 3, 5, 7],
            11: [2, 3, 5, 7, 11],
            12: [2, 3, 5, 7, 11],
        }
        for limit, expected in cases.items():
            with self.subTest(limit=limit):
                self.assertEqual(sieve(limit), expected)
                self.assertEqual(prime_count(limit), len(expected))

    def test_prime_squares_are_excluded(self):
        for square in (4, 9, 25, 49, 121):
            with self.subTest(square=square):
                self.assertNotIn(square, sieve(square))
                self.assertEqual(sieve(square), sieve(square - 1))
                self.assertEqual(prime_count(square), prime_count(square - 1))

    def test_known_prime_counts(self):
        self.assertEqual(prime_count(100), 25)
        self.assertEqual(prime_count(1_000_000), 78_498)

    def test_matches_independent_trial_division(self):
        expected = []
        for limit in range(251):
            if limit >= 2 and all(limit % divisor for divisor in range(2, limit)):
                expected.append(limit)
            with self.subTest(limit=limit):
                self.assertEqual(sieve(limit), expected)
                self.assertEqual(prime_count(limit), len(expected))

    def test_noninteger_inputs_raise_type_error(self):
        for value in (2.0, 2.5, "10", None, [10]):
            for function in (sieve, prime_count):
                with self.subTest(value=value, function=function.__name__):
                    with self.assertRaises(TypeError):
                        function(value)


if __name__ == "__main__":
    unittest.main()
