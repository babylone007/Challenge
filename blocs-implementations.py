import LogicGates as lg

def BL1(a, b, c):
    """
    Implementation of Block 1.
    """
    and1out = lg.AND(a, c)
    and2out = lg.AND(b, lg.NOT(c))
    s = lg.OR(and1out, and2out)
    return s


def BL2(a, b):
    """
    Implementation of Block 2.
    """
    orOut = lg.OR(a, b)
    s0 = orOut
    andOut = lg.AND(a, b)
    s1 = andOut
    xorOut = lg.XOR(a, b)
    s2 = xorOut
    return s0, s1, s2

def BL3(a, b, c):
    """
    Implementation of Block 3.
    """
    and1out = lg.AND(lg.NOT(a), b)
    and2out = lg.AND(a, c)
    s = lg.OR(and1out, and2out)
    return s

def BL4(a, b, c):
    """
    Implementation of Block 4.
    """
    and1out = lg.AND(a, b)
    and2out = lg.AND(lg.NOT(b), c)
    s = lg.OR(and1out, and2out)
    return s

def BL5(a, b, c):
    """
    Implementation of Block 5.
    """
    s0 = lg.XOR(b, c)
    andOut = lg.AND(b, c)
    s1 = lg.OR(a,andOut)
    return s0, s1

def BL6(a, b):
    """
    Implementation of Block 6.
    """
    and1out = lg.AND(a, lg.NOT(b))
    and2out = lg.AND(lg.NOT(a), b)
    s = lg.OR(and1out, and2out)
    return s

def BL7(a, b, c):
    """
    Implementation of Block 7.
    """
    and1out = lg.AND(a, lg.NOT(b))
    and2out = lg.AND(b, c)
    s = lg.OR(and1out, and2out)
    return s

"""
Testing ...
"""
# # Test BL1
# print("BL1 test :")
# print(BL1(0,0,0)) # 0
# print(BL1(0,1,0)) # 1
# print(BL1(0,0,1)) # 0
# print(BL1(1,1,0)) # 1
# print(BL1(1,1,1)) # 1
# # Test BL2
# print("BL2 test :")
# print(BL2(0,0)) # 000
# print(BL2(0,1)) # 101
# print(BL2(1,0)) # 101
# print(BL2(1,1)) # 110
# # Test BL3
# print("BL3 test :")
# print(BL3(0,0,0)) # 0
# print(BL3(0,1,0)) # 1
# print(BL3(0,0,1)) # 0
# print(BL3(1,1,0)) # 0
# print(BL3(1,1,1)) # 1
# # Test BL4
# print("BL4 test :")
# print(BL4(0,0,0)) # 0
# print(BL4(0,1,0)) # 0
# print(BL4(0,0,1)) # 1
# print(BL4(1,1,0)) # 1
# print(BL4(1,1,1)) # 1
# # Test BL5
# print("BL5 test :")
# print(BL5(0,0,0,0)) # 00
# print(BL5(0,1,0,1)) # 11
# print(BL5(0,0,1,1)) # 10
# print(BL5(1,1,0,0)) # 11
# print(BL5(1,1,1,1)) # 01
# # Test BL6
# print("BL6 test :")
# print(BL6(0,0)) # 0
# print(BL6(0,1)) # 1
# print(BL6(1,0)) # 1
# print(BL6(1,1)) # 0
# # Test BL7
# print("BL7 test :")
# print(BL7(0,0,0)) # 0
# print(BL7(0,1,0)) # 0
# print(BL7(0,0,1)) # 0
# print(BL7(1,1,0)) # 0
# print(BL7(1,1,1)) # 1
