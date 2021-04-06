#!/usr/bin/env python3

import FTree as ft

if __name__ == "__main__":
    z = ft.Gates()
    G4 = z.or_gate([["4"]], [["5"]])
    G5 = z.or_gate([["6"]], [["7"]])
    G6 = z.or_gate([["6"]], [["8"]])
    G2 = z.and_gate(G4, G5)
    G3 = z.or_gate([["3"]], G6)
    G1 = z.or_gate(G2, G3)
    G0 = z.or_gate([["1"]], z.or_gate(G1, [["2"]]))

    mcs = z.mcs(G0)
    z.pretty_display(mcs)
