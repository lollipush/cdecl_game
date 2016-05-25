#! /usr/bin/env python

from tokenizer import tokenizer

def main(argv):
    if len(argv) == 2:
        tks = list(tokenizer(argv[1]))
        for tk in tks:
            print tk

if __name__ == '__main__':
    import sys
    main(sys.argv)
