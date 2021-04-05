#!/usr/bin/env python3
import FTree as ft

if __name__ == "__main__":
    z = ft.Gates()
    G4 = z.or_gate([["b"]], [["c"]])
    G5 = z.and_gate([["a"]], [["b"]])
    G2 = z.or_gate([["a"]], G4)
    G3 = z.or_gate([["c"]], G5)
    top = z.and_gate(G3, G2)
    z.pretty_display(top)
    out = z.mcs(top)
    print(out)
    z.pretty_display(out)
    # distr = ft.Distributions()
    # calc_distr = distr.exp_dist(0, 5)
    # product = distr.prod_list([1.0, 0.4, 0.6])
    # print(f"value of product = {product}")
    # distr_dict = {
    # "a": 1 - distr.exp_dist(-0.5, 5),
    # "b": 1 - distr.exp_dist(-0.2, 5),
    # "c": 1.0,
    # "d": 1 - distr.exp_dist(-0.4, 5),
    # "e": 1 - distr.exp_dist(-0.3, 5),
    # "f": 1 - distr.exp_dist(-0.2, 5),
    # "g": 1 - distr.exp_dist(-0.3, 5),
    # "h": 1 - distr.exp_dist(-0.33, 5),
    # "i": 1 - distr.exp_dist(-0.2, 5),
    # }
    # prob_value = distr.prob(out, distr_dict)
    # print(prob_value)
