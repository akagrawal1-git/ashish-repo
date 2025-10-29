import math
import sys

def nth_prime(n: int) -> int:
    """Return the nth prime (1-based). Raises ValueError if n < 1."""
    if n < 1:
        raise ValueError("n must be >= 1")
    if n == 1:
        return 2

    # Rosser's theorem bound for nth prime for n >= 6; small n handled below
    if n < 6:
        limit = 15
    else:
        limit = int(n * (math.log(n) + math.log(math.log(n)))) + 3

    while True:
        sieve = bytearray(b'\x01') * (limit + 1)
        sieve[0:2] = b'\x00\x00'
        max_p = int(limit**0.5)
        for p in range(2, max_p + 1):
            if sieve[p]:
                start = p * p
                sieve[start:limit+1:p] = b'\x00' * (((limit - start) // p) + 1)

        count = 0
        for i, is_prime in enumerate(sieve):
            if is_prime:
                count += 1
                if count == n:
                    return i

        # If bound was too small (rare), increase and retry
        limit *= 2

if __name__ == "__main__":
    k = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    print(nth_prime(k))