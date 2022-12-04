#!/usr/bin/env python3
import sys
sys.path.insert(1,'../')
import FTree as ft

if __name__ == "__main__":
    z = ft.Gates()
    P_Sensor = z.or_gate([['E2'],['E3'],['E4'],['E5']],[['E6']])
    B_Sensor = z.or_gate([['E7'],['E8']],[['E9']])
    Sens_fail = z.and_gate(P_Sensor,B_Sensor)
    A = z.or_gate([['E1']],Sens_fail)

    mcs = z.mcs(A)

    z.pretty_display(mcs)
