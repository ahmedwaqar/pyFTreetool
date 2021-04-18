#!/usr/bin/env python3
import xml.etree.ElementTree as ET

xmlfile = 'diagrams/demo_ft.xml'

def remove_dup(input_list):
        out = []
        remove_duplicates = []
        for i in input_list:
            out.append(list(dict.fromkeys(i)))
        for dup in out:
            if dup not in remove_duplicates:
                remove_duplicates.append(dup)
        return [x[:] for x in remove_duplicates]

if __name__ == "__main__":
    tree = ET.parse(xmlfile)

    root = tree.getroot()

    # print(root.tag)

    ft = []
    # print(root.attrib)
    and_gate  =  '''
{} = z.and_gate({})
    '''
    or_gate  =  '''
{} = z.or_gate({})
    '''
    edges = []

    # for child in root.iter('mxCell'):
        # try:
            # if child.attrib['edge']:
                # edges+= child
        # except KeyError:
            # pass
    edges = root.findall(".//mxCell/[@edge]")
    sources = root.findall(".//mxCell/[@source]")
    for source in sources:
            source_ob = source.attrib['source']
            source_id = root.find(".//mxCell[@id='{}']".format(source_ob))
            target_id = source.attrib['target']
            gate = []
            # if source_id.attrib['value'] not in sources_list:
            gate.append(source_id.attrib['value'])
            for edge in edges:
                try:
                    if edge.attrib['source'] == source.attrib['source']:
                        target_temp = root.find(".//mxCell[@id='{}']".format(edge.attrib['target']))
                        edge_style = source_id.attrib['style']
                        if 'or' in edge_style:
                            gate_shape = 'or_gate'
                        else:
                            gate_shape = 'and_gate'
                        gate.append(gate_shape)
                        gate.append(target_temp.attrib['value'])
                except:
                    print(edge.attrib)
            ft.append(gate)
    ft = remove_dup(ft)
    for gates in ft:
        if 'and_gate' in gates[1]:
            print(and_gate.format(gates[0],gates[2:]))
        else:
            print(or_gate.format(gates[0],gates[2:]))

    print(ft)






        # temp = []
        # source = child.attrib['source']
        # temp.append(source)
        # source  = root.find(".//mxCell/[@id='{}']".format(source))
        # if 'xor' in source.attrib['style']:
            # temp.extend (source.attrib['style'])
        # target = child.attrib['target']
        # ids = root.find(".//mxCell/[@id='{}']".format(target))
        # temp += ids.attrib['value']
        # ft.append(temp)




