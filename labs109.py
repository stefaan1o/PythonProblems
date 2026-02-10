# 1
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


# 2
def is_ascending(items):
    for x in range(len(items) - 1):
        if items[x] >= items[x + 1]:
            return False

    return True


# 3
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


# 4
def only_odd_digits(n):
    for c in str(n):
        if int(c) % 2 == 0:
            return False
    return True


# 5
def is_cyclops(n):
    s = str(n)
    m = len(s) // 2

    if len(s) % 2 != 1:
        return False

    if s[m] != "0":
        return False

    if "0" in s[:m] or "0" in s[m + 1 :]:
        return False

    return True


# 6
def domino_cycle(tiles):
    if len(tiles) == 0:
        return True
    if tiles[0][0] != tiles[-1][1]:
        return False
    for x in range(len(tiles) - 1):
        if tiles[x][1] != tiles[x + 1][0]:
            return False
    return True


# 7
def colour_trio(colours):
    def mix(c1, c2):
        if c1 == c2:
            return c1
        return ({"r", "y", "b"} - {c1, c2}).pop()  # chatgpt

    while len(colours) > 1:
        colours = "".join(
            mix(colours[i], colours[i + 1]) for i in range(len(colours) - 1)
        )
    return colours


# 8
def count_dominators(items):
    max_so_far = float("-inf")
    out = 0
    for x in reversed(items):
        if x > max_so_far:
            out += 1
            max_so_far = x
    return out


# 9
def extract_increasing(digits):
    out = []
    previous = -1
    current = 0
    for c in digits:
        current = 10 * current + int(c)
        if current > previous:
            out.append(current)
            previous = current
            current = 0
    return out
