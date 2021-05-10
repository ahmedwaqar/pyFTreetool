import os, sys

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../')))
import FTree as ft

z = ft.Gates()
G4 = z.and_gate([['E8']] ,[['E9']])
G3 = z.or_gate([['E6']] ,[['E7']])

G2 = z.and_gate([['E3']] ,[['E4']],G3)
G1 = z.and_gate([['E1']] ,G2,G4,[['E5']])
mcs = z.mcs(G1)
z.pretty_display(mcs)

distr = ft.Distributions()

prob_value = distr.prob(mcs, {'E1': 0.2, 'E3': 0.2, 'E4': 0.2, 'E5': 0.2, 'E6': 0.2, 'E7': 0.2, 'E8': 0.2, 'E9': 0.2})
print(prob_value)
