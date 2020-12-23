
def compute_continued_fraction(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator should not be 0")
    #TODO: make recursive fn handle this
    list = []
    __compute(int(numerator), int(denominator), list)
    return list


def continued_fraction_from_real(real, precision):
    denominator = 10**precision
    return compute_continued_fraction(real*denominator,denominator)

def __compute(a, b, list):
    if b == 0:
        return
    if a == 0:
        list.append(0)
        return
    if b == 1:
        list.append(a)
        return
    list.append(a//b)
    __compute(b, a % b, list)


#TODO: restore as fraction
def restore(list):
    if len(list) == 1:
        return list.pop()
    return list.pop(0) + 1/restore(list)
