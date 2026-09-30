# Prime number sieve

A dependency-free Python 3.9+ implementation of the Sieve of Eratosthenes, with functions to list and count prime numbers up to an inclusive integer limit.

## Usage

```python
from primes import sieve, prime_count

sieve(30)        # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
prime_count(30)  # 10
```

Both functions include the upper bound. Limits below 2 return an empty list or zero; non-integer inputs raise `TypeError`.

Run the command-line example:

```sh
python3 primes.py 30
```

## How it works

The sieve stores one byte per number, initially marking every number except 0 and 1 as a candidate prime. For each remaining prime `p` up to the square root of the limit, it clears multiples starting at `p * p`; smaller multiples have already been cleared by smaller primes.

`sieve` collects the numbers still marked as prime. `prime_count` sums the same flags without building a list of primes. Each function takes **O(n log log n)** time and **O(n)** memory, where `n` is the limit.

## Tests

```sh
python3 -m unittest -v
```

The tests cover inclusive boundaries, limits below 2, prime squares, invalid inputs, agreement with independent trial division, and known counts including 78,498 primes through 1,000,000.
