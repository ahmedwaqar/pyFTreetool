#!/usr/bin/env python3
import FTree as ft

if __name__ == "__main__":
    z = ft.Gates()
    pump_A = z.or_gate([["M"]], [["W"]])
    pump_B = z.or_gate([["M"]], [["Z"]])
    pump = z.and_gate(pump_A, pump_B)
    mcs = z.mcs(pump)
    z.pretty_display(mcs)
