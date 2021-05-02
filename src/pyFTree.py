#!/usr/bin/env python3
import argparse
import subprocess as sp

if __name__ == "__main__":

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h", "--help",action="help", help="Specify fault tree program path as an argument to FT_parser, e.g., ./FT_parser.py ft_program.py")
    # parser.add_argument("ft_path", default=argparse.SUPPRESS, help="Provide a path to FT program")
    parser.add_argument("-X", "--xml", action="store_true", help="Parse the xml diagram file")
    args = parser.parse_args()

    # if args.ft_path:
        # f_path = args.ft_path

    if args.xml:
        sp.run("./xml_parser_ft.py")
        with open("cutsets.txt", "w") as f:
            sp.call(["python3","ft_prog.py"], stdout=f)

    # gen_ft = GenerateFT()
    # gen_ft.print_FT(f_path)
