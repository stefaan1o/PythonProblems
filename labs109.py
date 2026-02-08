def ryerson_letter_grade(n):
    if n < 50:
        return "F"
    elif n > 89:
        return "A+"
    elif n > 84:
        return "A"
    elif n > 79:
        return "A-"
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust


def is_ascending(items):
    for x in range(len(items) - 1):
        if items[x] >= items[x + 1]:
            return False

    return True


def riffle(items, out=True):
    o = []
    y = len(items) // 2
    if len(items) > 0:
        for x in range(y):
            if out:
                o += [items[x], items[x + y]]
            else:
                o += [items[x + y], items[x]]
    return o


def only_odd_digits(n):
    for c in str(n):
        if int(c) % 2 == 0:
            return False
    return True
