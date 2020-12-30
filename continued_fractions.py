def compute_continued_fraction(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator should not be 0")
    # TODO: Make a recursive fn to return the expansion
    expansion = []
    __compute(int(numerator), int(denominator), expansion)
    return expansion


def continued_fraction_from_real(real, precision):
    denominator = 10 ** precision
    return compute_continued_fraction(real * denominator, denominator)


def __compute(a, b, expansion):
    if b == 0:
        return
    if a == 0:
        expansion.append(0)
        return
    if b == 1:
        expansion.append(a)
        return
    expansion.append(a // b)
    __compute(b, a % b, expansion)


def restore(expansion):
    return __restore(expansion, 0)


def __restore(expansion, n):
    if n == len(expansion) - 1:
        return expansion[n]
    return expansion[n] + 1.0 / __restore(expansion, n + 1)
