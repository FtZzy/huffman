#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from compress import compress
from decompress import decompress


def display_doc(*args):
    """
    Display the documentation of the program.
    """
    print("""For compress <my_file.txt>:
    $ python huffman.py -c <my_file.txt>
For decompress <my_file.bin>:
    $ python huffman.py -c <my_file.bin>""")


if __name__ == '__main__':
    """Huffman algorithm."""
    try:
        arg = sys.argv[1]
        choices = {
            '-c': compress,
            '-d': decompress
        }
        choices.get(arg)(sys.argv[2])
    except IndexError as e:
        print("You need to give a correct argument and a filename, %s! See the documentation:" % e)
        display_doc()
    else:
        print("Finished.")
