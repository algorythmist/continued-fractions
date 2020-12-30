
def compute_continued_fraction(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator should not be 0")
    return __compute(int(numerator), int(denominator))


def __compute(a, b):
    if b == 0:
        return []
    if a == 0:
        return [0]
    return [a//b] + __compute(b, a % b)


def continued_fraction_from_real(real, precision):
    denominator = 10 ** precision
    return compute_continued_fraction(real * denominator, denominator)

def restore(expansion):
    return __restore(expansion, 0)


def __restore(expansion, n):
    if n == len(expansion) - 1:
        return expansion[n]
    return expansion[n] + 1.0 / __restore(expansion, n + 1)
