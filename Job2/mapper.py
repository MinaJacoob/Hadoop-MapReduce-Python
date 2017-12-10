#!/usr/bin/env python
from __future__ import print_function  # to avoid default new line printing

import sys


def mapper():
    for line in sys.stdin:
        line.strip()
        print(line, end='')


print('end', '\t', 'end')  # print to the end of the stream to mark the end of the data

if __name__ == '__main__':
    mapper()
