#! /usr/bin/env python

from tokenizer import tokenizer
from parser import parser, read_bnf, print_bnf

def main(argv):
    if len(argv) >= 2:
        with open(argv[1], 'r') as f:
            grammar = read_bnf(f.read())
        print_bnf(grammar)
        if len(argv) >= 3:
            tks = list(tokenizer(argv[1]))
            for tk in tks:
                print tk
            print
            ast = parser(tks)
            print ast

if __name__ == '__main__':
    import sys
    main(sys.argv)
