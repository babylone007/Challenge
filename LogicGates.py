def AND (a, b):
    """
    AND Logic gate
    """
    if a == 1 and b == 1:
        return 1
    else:
        return 0


def OR (a, b):
    """
    OR Logic gate
    """
    if a == 0 and b == 0:
        return 0
    else:
        return 1

def XOR (a, b):
    """
    XOR Logic gate
    """
    if a != b:
        return 1
    else:
        return 0

def NOT (a):
    """
    Inversor gate
    """
    if (a == 0):
        return 1
    elif (a == 1):
        return 0


# TESTS
# print(lg.XOR (0,0))
# print(lg.XOR (0,1))
# print(lg.XOR (1,0))
# print(lg.XOR (1,1))
# print(lg.NOT(1))
# print(lg.NOT(0))
