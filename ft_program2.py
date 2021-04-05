#!/usr/bin/env python3
import FTree as ft

if __name__ == "__main__":
    z = ft.Gates()
    G1 = z.and_gate([["PT1"]], [["PT2"]])
    G2 = z.and_gate([["PT1"]], [["PT3"]])
    G3 = z.and_gate([["PT3"]], [["PT2"]])
    G4 = z.or_gate(G1, z.or_gate(G2, G3))
    G5 = z.or_gate([["SDV1"]], [["SDV2"]])
    top = z.or_gate(G4, z.or_gate([["LS"]], G5))
    print(top)
    mcs = z.mcs(top)
    z.pretty_display(mcs)
