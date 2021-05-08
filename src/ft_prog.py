import FTree as ft

z = ft.Gates()
G4 = z.and_gate([['E8']] ,[['E9']])
G3 = z.or_gate([['E6']] ,[['E7']])

G2 = z.and_gate([['E3']] ,[['E4']],G3)
G1 = z.and_gate([['E1']] ,G2,G4,[['E5']])
mcs = z.mcs(G1)
z.pretty_display(mcs)
