import sys
sys.path.insert(1,'../')
import FTree as ft

if __name__ == "__main__":
    z = ft.Gates()
    G1 = z.or_gate([['x1']],[['x2']])
    G2 = z.or_gate([['x1']],[['x2']])
    G3 = z.or_gate([['x3']],G2)
    G4 = z.or_gate([['x7']],[['x8']])
    G5 = z.or_gate(G1,G2)
    G6 = z.or_gate(G5,G4)
    mcs = z.mcs(G6)
    z.pretty_display(mcs)
