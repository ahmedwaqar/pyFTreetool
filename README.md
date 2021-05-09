# Introduction
The pyFTree is a open source tool that takes a FT model as a python program and spit out minimal cutsets.
To generate a fault tree, use ``FT_parser`` and provide the path of the program file.

## Installation

### Linux

A quick way to install the pyFTree as a python package is to follow the following instructions:

1. At terminal, execute `git clone https://github.com/ahmedwaqar/pyFTreetool`
2. `cd pyFTreetool && sudo python setup.py install`

## Documentation

### Usage

One of the two approaches can be used to perform FTA using pyFTreetool.

### Approach 1: Draw and Analyze

pyFTreetool provides a `xml_parser` that can take a fault tree diagram drawn using `draw.io` and exported in a XML format.
The choice of `draw.io` is mainly for its open source features available both in web and desktop version.
However, not all the styles of fault tree diagrams should be parsed by `xml_parser`, there must be some rules lay down so that
users can successuly generate python code for given FT diagram. An easy way to learn this approach is consider an exmaple FT
shown in the figure below. The details of each FT node and the resulting cutsets are described in [1].

![Composite Laminate Structure](/src/diagrams/examplediag.png)




**Disclaimer** Its a fun project and in an early stage of the development. The `FTree.py` and `FT_parser.py` expectedly contains bugs that would be uncovered as the project goes to the next stages.

**Contributions**: The suggestions/contributions are welcome and could be pushed in through pull request.
A feature request can also be made by opening issues.
