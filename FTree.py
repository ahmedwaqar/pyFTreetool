#!/usr/bin/env python3
from abc import ABC
import math
import itertools


class AbstractGates(ABC):
    def and_gate(self):
        pass

    def or_gate(self):
        pass


class Gates(AbstractGates):
    '''Mocus algorithm is encoded in the defns of and_gate and or_gate and
    finally a call to mcs remove the duplicate within the cutsets and also reduce the cutsets to minimal'''
    def __init__(self):
        pass

    def and_gate(self, lnodes, rnodes, *args):
        '''add nodes to each of cutsets'''
        temp = []
        for i in lnodes:
            for r in rnodes:
                temp.append(i + r)
        out1 = []
        if args:
            for arg in args:
                for a1 in arg:
                    for t in temp:
                        out1.append(t + a1)
            return out1
        else:
            return temp

    def or_gate(self, lnodes, rnodes, *args):
        '''extend cutsets'''
        out = [x[:] for x in lnodes]
        out += rnodes
        for arg in args:
            for a1 in arg:
                out.append(a1)
        return out

    def sort_sublists(self, input_list):
        result = list(map(sorted, input_list))
        return result

    def mcs(self, cut_set):
        out = []
        remove_duplicates = []
        cut_sets = self.sort_sublists(cut_set)
        for i in cut_sets:
            out.append(list(dict.fromkeys(i)))
        for cut_set in out:
            if cut_set not in remove_duplicates:
                remove_duplicates.append(cut_set)
        minimal_cuts = [x[:] for x in remove_duplicates]
        for a, b in itertools.combinations(minimal_cuts, 2):
            try:
                if set(a) <= set(b):
                    minimal_cuts.remove(b)
                elif set(b) <= set(a):
                    minimal_cuts.remove(a)
            except:
                continue
        return minimal_cuts

    def pretty_display(self, cut_sets):
        for i in range(len(cut_sets)):
            print("mcs_{}={}\n".format(i, cut_sets[i]))


class Distributions(Gates):
    def __init__(self):
        pass

    def exp_dist(self, rate, t):
        return math.exp(rate * t)

    def prod_list(self, iterlist):
        result = 1
        for x in iterlist:
            result *= 1 - x
        return result

    def prob(self, mcs, distr_dict):
        prob_calc = 0
        for cut_set in mcs:
            prob_list = []
            for event in cut_set:
                prob_list.append(distr_dict[f"{event}"])
            prob_calc += self.prod_list(prob_list)
        return 1 - prob_calc
