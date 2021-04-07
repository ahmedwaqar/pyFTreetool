#!/usr/bin/env python3
import sys
sys.path.insert(1,'../')
import FTree as ft

if __name__ == "__main__":
    z = ft.Gates()
    node_4 = z.or_gate([['F']],[['G']])
    node_5 = z.and_gate([['H']],[['I']])
    node_2 = z.or_gate(node_4,z.or_gate([['B']],[['C']]))
    node_3 = z.or_gate(z.or_gate([['C']],[['D']]), node_5)
    node_1 = z.and_gate(node_2,node_3)
    mcs = z.mcs(node_1)
    z.pretty_display(mcs)

