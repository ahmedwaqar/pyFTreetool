import FTree as ft

z = ft.Gates()
G2 = z.or_gate([['E3']] ,[['E4']])
G1 = z.and_gate([['E1']] ,G2)
mcs = z.mcs(G1)
z.pretty_display(mcs)