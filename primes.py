"""Find and count primes up to an inclusive integer limit."""

from math import isqrt


def _sieve_flags(limit: int) -> bytearray:
    """Return flags whose indices are numbers and whose values mark primes."""
    if not isinstance(limit, int):
        raise TypeError("limit must be an integer")
    if limit < 2:
        return bytearray()

    # Start with every number as a candidate, then exclude 0 and 1.
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0] = flags[1] = 0

    for prime in range(2, isqrt(limit) + 1):
        if flags[prime]:
            # Smaller multiples already have a smaller prime factor.
            start = prime * prime
            count = (limit - start) // prime + 1
            flags[start : limit + 1 : prime] = b"\x00" * count

    return flags


def sieve(limit: int) -> list[int]:
    """Return all primes <= limit using the Sieve of Eratosthenes.

    Limits below 2 return an empty list. Non-integer limits raise TypeError.
    Time: O(limit * log(log(limit))). Space: O(limit).
    """
    return [number for number, is_prime in enumerate(_sieve_flags(limit)) if is_prime]


def prime_count(limit: int) -> int:
    """Return the number of primes <= limit, conventionally written pi(limit).

    Limits below 2 return 0. Non-integer limits raise TypeError.
    Uses the same sieve without constructing a list of prime numbers.
    Time: O(limit * log(log(limit))). Space: O(limit).
    """
    return sum(_sieve_flags(limit))


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description=__doc__)
    parser.add_argument("limit", type=int, help="inclusive upper bound")
    args = parser.parse_args()
    primes = sieve(args.limit)
    print(f"Primes <= {args.limit}: {primes}")
    print(f"Prime count: {len(primes)}")
