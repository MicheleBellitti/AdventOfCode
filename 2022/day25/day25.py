data = open('./input#25.txt', 'r').readlines()


def toDec(s):
    """Converts a SNAFU-encoded number to a decimal number."""
    s = s.replace('\n', '')
    l = len(s)
    ss = 0
    for i, c in enumerate(s):

        if c == '-':
            c = -1
        elif c == '=':
            c = -2
        else:
            c = int(c)
        ss += c * (5 ** (l - i - 1))
    return ss


def toSNAFU(n):
    """Converts a number to a SNAFU string."""
    s = ''
    carry = 0
    while n > 0:

        r = n % 5
        if carry != 0:
            r += carry
            carry = 0
        if r > 2:
            carry += 1
            r -= 5
        if r == -1:
            s += '-'
        elif r == -2:
            s += '='
        else:
            s += str(r)
        n = n // 5

    return s[::-1]


sols = [toDec(s) for s in data]

print(toSNAFU(sum(sols)))
