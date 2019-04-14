# import LogicGates as lg
import block-implementation as blk

def FC1 (A0, A1, A2, A3, A4, A5, A6, A7, BB3):
    """
    Implementation of Function 1, it's composed of 7 BL1 and 1 BL7.
    """
    BL11_out = blk.BL1(A6, A7, BB3)
    BL12_out = blk.BL1(A5, A6, BB3)
    BL13_out = blk.BL1(A4, A5, BB3)
    BL14_out = blk.BL1(A3, A4, BB3)
    BL15_out = blk.BL1(A2, A3, BB3)
    BL16_out = blk.BL1(A1, A2, BB3)
    BL17_out = blk.BL1(A0, A1, BB3)

    BL71_out = blk.BL7(A0, A7, B33)
    return BL11_out, BL12_out, BL13_out, BL14_out, BL15_out, BL16_out, BL17_out, BL71_out


def FC2 (B0, B1, B2, B3, B4, B5, B6, B7, BB3):
    """
    Implementation of Function 1, it's composed of 7 BL1 and 1 BL7.
    """
    BL18_out = blk.BL1(B6, B7, BB4)
    BL19_out = blk.BL1(B5, B6, BB4)
    BL110_out = blk.BL1(B4, B5, BB4)
    BL111_out = blk.BL1(B3, B4, BB4)
    BL112_out = blk.BL1(B2, B3, BB4)
    BL113_out = blk.BL1(B1, B2, BB4)
    BL114_out = blk.BL1(B0, B1, BB4)

    BL72_out = blk.BL7(B0, B7, B33)
    return BL18_out, BL19_out, BL110_out, BL111_out, BL112_out, BL113_out, BL114_out, BL72_out


def FC3 (BB1, BB2, OP0, OP1):
    """
    Implementation of Function 3 which is composed of 2 BL6.
    """
    BL61_out = blk.BL6(OP0, BB1)
    BL62_out = blk.BL6(OP1, BB2)

    FC3_out0 = BL61_out
    FC3_out1 = BL62_out

    return FC3_out0, FC3_out1

def FC4 (FC2_si, FC1_si, FC3_s0, FC3_s1, FC4_siPlus1):
    """
    Implementation of Function 1, it's composed of 7 BL1 and 1 BL7.
    """
    BL2_out = blk.BL2(FC2_si, FC1_si)
    BL5_out = blk.BL5(BL2_out[1], BL2_out[2], FC4_siPlus1)
    s0 = BL5_out[1]
    BL31_out = blk.BL2(FC3_s0, BL2_out[2], BL5_out[0])
    BL4_out = blk.BL4(BL2_out[0], FC3_s0, BL2_out[1])
    BL32_out = blk.BL3(FC3_s1, BL4_out, BL31_out)
    s1 = BL32_out
    return s0, s1
