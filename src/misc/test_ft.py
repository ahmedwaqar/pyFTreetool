import FTree as ft



z = ft.Gates()
G1 = z.and_gate([['E1']],[['E2']],[['E3']])
G2 = z.or_gate([['E1']],[['E2']],G1)
G3 = z.and_gate([['E1']],G2,G1)
print(G3)
