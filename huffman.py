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
        file_path = sys.argv[2]
    except IndexError as e:
        print("You need to give an argument and a filename!\n" % e)
        print("See the documentation:")
        display_doc()
    else:
        choices = {
            '-c': compress,
            '-d': decompress,
        }
        choices.get(arg, display_doc)(file_path)
    finally:
        print("Program finished.")
