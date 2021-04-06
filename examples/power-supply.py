#!/usr/bin/env python3
import FTree as ft

if __name__ == "__main__":
    z = ft.Gates()
    top = z.and_gate(
        z.or_gate([["A"]], [["B"]]),
        z.or_gate(
            z.and_gate(z.or_gate([["C"]], [["D"]]), z.or_gate([["E"]], [["C"]])),
            z.and_gate([["D"]], [["E"]]),
        ),
    )

    mcs = z.mcs(top)

    z.pretty_display(mcs)
