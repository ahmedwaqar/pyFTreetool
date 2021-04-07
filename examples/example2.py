#!/usr/bin/env python3
import sys

sys.path.insert(1, "../")
import FTree as ft

if __name__ == "__main__":
    z = ft.Gates()
    # Node 20 Subtree
    node_20 = z.or_gate([["node_90"]], [["node_91"]])
    # Node 47 Subtree
    node_47 = z.or_gate([["node_49"], ["node_30"]], node_20)
    # Node 19 Subtree
    node_19 = z.or_gate([["node_26"]], [["node_27"]])
    # Node 23 Subtree
    node_84 = z.or_gate([["node_85"], ["node_86"]], [["node_87"]])
    node_80 = z.and_gate([["node_82", "node_83"]], node_84)
    node_43 = z.and_gate([["node_81"]], node_80)
    node_23 = z.or_gate(z.or_gate(node_20, node_43), [["node_45"], ["node_44"]])
    # Node 6 Subtree
    node_6 = z.or_gate(
        [["node_11"], ["node_12"], ["node_13"], ["node_17"], ["node_18"], ["node_70"]],
        [["node_14"], ["node_15"], ["node_16"]],
    )
    # Node 21 Subtree
    node_31 = z.or_gate(z.or_gate(node_23, node_19), node_20)
    node_33 = z.or_gate([["node_35"]], [["node_36"]])
    node_28 = z.or_gate([["node_32"], ["node_34"]], node_33)
    node_21 = z.or_gate(
        [["node_55"], ["node_29"], ["node_30"]],
        z.or_gate(node_6, z.or_gate(node_31, node_28)),
    )
    # Node 24 Subtree
    node_24 = z.or_gate(
        z.or_gate(node_6, node_23),
        z.or_gate(node_19, z.or_gate(node_20, [["node_29"]])),
    )
    # Node 7 Subtree
    node_7 = z.or_gate(node_19, z.or_gate(node_21, z.or_gate(node_20, node_24)))
    # Node 38 Subtree
    node_38 = z.or_gate(
        node_19, z.or_gate(node_21, z.or_gate(node_20, z.or_gate(node_24, node_47)))
    )
    # Node 39 Subtree
    node_39 = z.or_gate(
        node_19, z.or_gate(node_21, z.or_gate(node_20, z.or_gate(node_24, node_47)))
    )
    # Node 48 Subtree
    node_92 = z.or_gate(node_19, z.or_gate(node_21, node_23))
    node_52 = z.or_gate(node_19, node_21)
    node_40 = z.or_gate(node_52, [["node_51"]])
    node_41 = z.or_gate(node_19, node_21)
    node_42 = z.or_gate(node_19, node_21)
    node_48 = z.or_gate(node_92, z.or_gate(node_40, z.or_gate(node_41, node_42)))
    # Node 9 Subtree
    node_37 = z.or_gate(node_48, z.or_gate(node_20, node_24))
    node_9 = z.or_gate(node_38, z.or_gate(node_37, node_39))
    # Top-level Event for Hazard 2
    node_65 = z.or_gate(node_19, z.or_gate(node_21, z.or_gate(node_20, node_24)))
    node_63 = z.or_gate([["node_67"], ["node_10"]], node_9)
    node_61 = z.or_gate([["node_64"]], node_65)
    node_60 = z.and_gate(node_61, z.and_gate([["node_62"]], node_63))
    # Top-level Event for Hazard 1
    node_2 = z.or_gate(
        node_7, z.or_gate([["node_29"]], z.or_gate(node_6, [["node_5"]]))
    )
    node_4 = z.or_gate(node_9, [["node_10"]])
    top = z.and_gate(node_2, z.and_gate([["node_3"]], node_4))

    # Minimal cutset calculation
    mcs = z.mcs(node_60)

    z.pretty_display(mcs)
    # Note: node 71 are not present in the original model
