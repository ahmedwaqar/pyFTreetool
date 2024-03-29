#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import itertools
import sys
import toml
from operator import itemgetter

xmlfile = sys.argv[1]

# xmlfile = 'diagrams/demo_ft.xml'
output_path = sys.argv[2]
and_gate  =  '''
{} = z.and_gate({} '''
or_gate  =  '''
{} = z.or_gate({} '''
boiler_plate = '''import os, sys

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../')))
import FTree as ft

z = ft.Gates()'''
boiler_plate_end = '''mcs = z.mcs(G1)
z.pretty_display(mcs)
'''
prob_bp = '''
distr = ft.Distributions()
'''

prob_bp_end = '''
prob_value = distr.prob(mcs, {})
print(prob_value)
'''

class xml_parser():
    def __init__(self):
        pass

    def remove_dup_iter(self, nodes):
        # nodes.sort(key=itemgetter(0))
        # sorted(nodes)
        return list(k for k,_ in itertools.groupby(nodes))

    def get_target(self, root, source, edges):
        for edge in edges:
            if edge.attrib['source'] == source.attrib['id']:
                target = root.find(".//mxCell[@id='{}']".format(edge.attrib['target']))
                # print(edge.attrib)
                break
            else:
                target = None
        return target


    def parse_xml(self, xfile):
        tree = ET.parse(xfile)

        root = tree.getroot()


        ft = []
        edges = []

        edges = root.findall(".//mxCell/[@edge]")
        sources = root.findall(".//mxCell/[@source]")
        for source in sources:
                source_ob = source.attrib['source']
                source_id = root.find(".//mxCell[@id='{}']".format(source_ob))
                gate = []
                if ('or' in source_id.attrib['style']) | ('and' in source_id.attrib['style']):
                    gate.append(source_id.attrib['value'])
                else:
                    # self.get_target(root, source, edges))
                    continue

                gate.append('=')
                for edge in edges:
                    try:
                        if edge.attrib['source'] == source.attrib['source']:
                            target_temp = root.find(".//mxCell[@id='{}']".format(edge.attrib['target']))
                            edge_style = source_id.attrib['style']
                            if 'or' in edge_style:
                                gate_shape = 'or_gate'
                            else:
                                gate_shape = 'and_gate'
                            if gate_shape not in gate:
                                gate.append(gate_shape)
                            node_gate = target_temp
                            node_target = self.get_target(root, node_gate, edges)
                            if 'or' in node_gate.attrib['style']:
                                gate.append(node_gate.attrib['value'])
                            elif 'and' in node_gate.attrib['style']:
                                gate.append(node_gate.attrib['value'])
                            elif node_target:
                                gate.append(node_target.attrib['value'])
                            else:
                                gate.append(f"[['{node_gate.attrib['value']}']]")
                    except:
                        # print(edge.attrib)
                        pass
                ft.append(gate)
        return ft

    def gen_ft_program(self,ft):
        with open(output_path,'w') as file:
            file.write(boiler_plate)
            for gates in ft:
                if 'and_gate' in gates[2]:
                    file.write(and_gate.format(gates[0],gates[3]))
                    for g in gates[4:]:
                        file.write(',' + g)
                    file.write(')')
                else:
                    file.write(or_gate.format(gates[0],gates[3]))
                    for g in gates[4:]:
                        file.write(',' + g)
                    file.write(')')
                    file.write('\n')
            file.write('\n')
            file.write(boiler_plate_end)
            config = toml.load('conf.toml')
            if config['enabled']:
                file.write(prob_bp)
                distr_dict = config['failure_rates']
                file.write(prob_bp_end.format(distr_dict))



if __name__ == "__main__":
    xparser = xml_parser()
    ft = xparser.parse_xml(xmlfile)
    ft = xparser.remove_dup_iter(ft)
    # ft.sort()
    # sorted(ft, key=itemgetter(3,4))
    # print(ft_rev)
    ft.reverse()
    xparser.gen_ft_program(ft)



