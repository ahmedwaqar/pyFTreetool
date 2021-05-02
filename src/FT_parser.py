#!/usr/bin/env python3
import re
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import sys
import argparse
# import Image


# f_path = 'ft_program.py'


class GenerateFT:
    def __init__(self):
        pass

    def remove_spaces(self,nodes):
        for node in nodes:
            for n in node:
                if n == '':
                    node.remove('')
        return nodes

    def partition_cond(self, ft_list, cond):
        new_list = []
        part_list = []
        for x in ft_list:
            if x == cond:
                new_list.append(part_list)
                part_list = []
                continue
            part_list.append(x)
        return new_list

    def add_nodes(self, G, list):
        G.add_nodes_from(list)

    def add_edges(self, G, list):
        edge_list = []
        try:
            if list:
                edge_list = edge_list + ([(list[0], list[1])])
        except:
            raise Exception
        for x in list[2:]:
            edge_list = edge_list + ([(list[1], x)])
            if ('and' in x) | ('or' in x):
                edge_list = edge_list + ([(x,list[list.index(x) + 1])])
        G.add_edges_from(edge_list)

    def filter_comments(self, txt):
        return [i for i in txt if not re.search(r'\#',i)]

    def gates_regex(self, _file):
        regex = r'([a-zA-Z]+\.((and)|(or))_gate)'
        return [lines for lines in _file if re.search(regex, lines)]

    def strip_gates_param(self, txt):
        frag = []
        txt_t = []
        for t in txt:
            txt_t.append(t.splitlines())
        for i in txt_t:
            frag.append(re.split(r'=|,|\(|\)', i[0]))
        frag_t1 = []
        for f in frag:
            frag_t1.append([r.strip() for r in f])
        for r in frag_t1:
            for i in range(len(r)):
                if '[' in r[i]:
                    r[i] = r[i].split(r'[["')[-1]
                    r[i] = r[i].split(r'[[')[-1]
                    r[i] = r[i].split(r'["')[-1]
                if ']' in r[i]:
                    r[i] = r[i].split(r'"]]')[0]
                    r[i] = r[i].split(r']]')[0]
                    r[i] = r[i].split(r'"]')[0]
                else:
                    continue
        return frag_t1

    def index_gates(self, nodes):
        index = 1
        for node in nodes:
            for i in range(len(node)):
                if node[i] == "z.and_gate" or node[i] == "z.or_gate":
                        node[i] = node[i].split('.')[-1].split('_')[0] + ' ' + '(G' + str(index) + ')'
                        index += 1
            else:
                continue
        return nodes

    def plot_graph_ft(self, parsed_ft):
        # n_size = 320
        G = nx.DiGraph()
        for i in parsed_ft:
            self.add_nodes(G, i)
            self.add_edges(G, i)
        plt.figure(figsize=(15, 45))
        plt.subplot(111)
        # write_dot(G, 'test.dot')

        # same layout using matplotlib with no labels
        plt.title('Fault Tree Diagram')
        pos = graphviz_layout(G, prog='dot')
        nx.draw_networkx(
            G,
            pos=pos,
            with_labels=True,
            # node_size=[len(v) * n_size for v in G.nodes()],
            alpha=0.3,
            arrows=True,
            arrowsize=20,
            width=2,
            bbox=dict(facecolor="skyblue", edgecolor='black', boxstyle='round,pad=0.2'),
        )
        # draw white circles over the lines
        nx.draw_networkx(
            G,
            pos=pos,
            with_labels=True,
            # node_size=[len(v) * n_size for v in G.nodes()],
            alpha=1,
            arrows=True,
            arrowsize=20,
            width=2,
            node_color='w',
            bbox=dict(facecolor="skyblue", edgecolor='black', boxstyle='round,pad=0.2'),
        )
        # draw the nodes as desired
        nx.draw_networkx(
            G,
            pos=pos,
            # node_size=[len(v) * n_size for v in G.nodes()],
            alpha=0.3,
            arrows=True,
            arrowsize=20,
            width=2,
            bbox=dict(facecolor="skyblue", edgecolor='black', boxstyle='round,pad=0.2'),
        )
        nx.draw_networkx_labels(G, pos=pos)
        plt.axis("off")
        plt.savefig('fault_tree.png')
        # Image.open('fault_tree.png').save('fault_tree.jpg','JPEG')# plt.show()

    def print_FT(self, file_path):
        with open(file_path) as file:
            # clean the data extracted from program file
            clean_ft = self.filter_comments(file)
            gates_search = self.gates_regex(clean_ft)
            ft_frag = self.strip_gates_param(gates_search)
            ft_frag = self.index_gates(ft_frag)
            part_ft = self.remove_spaces(ft_frag)
            part_ft = self.remove_spaces(ft_frag)
            self.plot_graph_ft(part_ft)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h", "--help",action="help", help="Specify fault tree program path as an argument to FT_parser, e.g., ./FT_parser.py ft_program.py")
    parser.add_argument("ft_path", default=argparse.SUPPRESS, help="Provide a path to FT program")
    args = parser.parse_args()

    if args.ft_path:
        f_path = args.ft_path
    gen_ft = GenerateFT()
    gen_ft.print_FT(f_path)
