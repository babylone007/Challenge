import blocksFunction as bkfc


def schematic(A,B, BB, OP):
    """
    Global Execution function.
    """
    # FC4_GlobalBloc(A,B, BB, OP)

    FC1_out = bkfc.FC1(A0, A1, A2, A3, A4, A5, A6, A7, BB3)
    FC2_out = bkfc.FC2(B0, B1, B2, B3, B4, B5, B6, B7, BB3)
    FC3_out = blkf.FC3(BB1, BB2, OP0, OP1)
    """
    TODO
    FC41 = bkfc.FC4(FC2_si, FC1_si, FC3_s0, FC3_s1, FC4_siPlus1)
    ....
    FC48 = ...
    """
    return out, s0
