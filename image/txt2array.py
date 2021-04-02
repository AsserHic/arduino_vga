#!/usr/bin/env python3

import fileinput


def read_image():
    row = -1
    for line in fileinput.input():
        if row < 0:
           print(line)
           row = 0
           continue
        elements = line.split()
        pos = [int(value) for value in elements[0][:-1].split(',')]
        if pos[1] != row:
           row += 1
           print(row)

if __name__ == '__main__':
    read_image()

