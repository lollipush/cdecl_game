#! /usr/bin/env python

from tokenizer import tokenizer
from parser import parser

def main(argv):
    if len(argv) == 2:
        tks = list(tokenizer(argv[1]))
        for tk in tks:
            print tk
        print
        ast = parser(tks)
        print ast

if __name__ == '__main__':
    import sys
    main(sys.argv)
