#!/usr/bin/env python3
import sys
sys.path.insert(1,'../')
import FTree as ft

if __name__ == "__main__":
    z = ft.Gates()
    C1 = z.and_gate([['D1']],[['D2']])
    C2 = z.and_gate([['D1']],z.or_gate([['D3']],[['D4']]))
    C3 = z.and_gate([['D5']],z.or_gate([['D2']],[['D6']]))
    C4 = z.and_gate([['D1']],[['D7']])
    B1 = z.or_gate(C1,z.or_gate(C2,z.or_gate(C3,C4)))

    C5 = z.and_gate([['D5']],z.or_gate([['D2']],[['D6']]))
    C6 = z.and_gate([['D8']],z.or_gate([['D2']],z.or_gate([['D4']],[['D6']])))
    C7 = z.and_gate([['D8']],z.or_gate([['D4']],[['D9']]))
    B2 = z.or_gate(C5,z.or_gate(C6,C7))
    A = z.and_gate(B1,B2)

    mcs = z.mcs(A)

    z.pretty_display(mcs)


