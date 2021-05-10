import os, sys

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../')))
import FTree as ft

z = ft.Gates()
G15 = z.or_gate([['D4']] ,[['D9']])

G10 = z.and_gate([['D8']] ,G15)
G14 = z.or_gate([['D2']] ,[['D4']],[['D6']])

G9 = z.and_gate([['D8']] ,G14)
G13 = z.or_gate([['D2']] ,[['D6']])

G8 = z.and_gate([['D5']] ,G13)
G3 = z.or_gate(G8 ,G9,G10)

G7 = z.and_gate([['D7']] ,[['D1']])
G12 = z.or_gate([['D2']] ,[['D6']])

G6 = z.and_gate([['D5']] ,G12)
G11 = z.or_gate([['D3']] ,[['D4']])

G5 = z.and_gate(G11 ,[['D1']])
G4 = z.and_gate([['D1']] ,[['D2']])
G2 = z.or_gate(G4 ,G6,G7,G5)

G1 = z.and_gate(G2 ,G3)
mcs = z.mcs(G1)
z.pretty_display(mcs)
