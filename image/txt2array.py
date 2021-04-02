#!/usr/bin/env python3

import fileinput


def read_image():
    row = -1
    cols = []
    for line in fileinput.input():
        if row < 0:
           print(line.strip())
           row = 0
           continue
        elements = line.split()
        pos = [int(value) for value in elements[0][:-1].split(',')]
        if pos[1] != row:
           row = pos[1]
           yield cols
           cols = []
        cols.append(elements[2])
    yield cols

def create_color_map(rows):
    colors = set()
    for row in rows:
        colors.update(row)
    if len(colors) != 4:
        print(f"Expected exactly 4 colors: {', '.join(colors)}.")
        exit(1)
    return {color: i for i, color in enumerate(sorted(colors, reverse=True))}

def collapse_pixels(rows, color_map):
    for row in rows:
        row = [color_map[value] for value in row]
        collapsed = []
        for i in range(0, len(row), 4):
            collapsed.append(sum([
                row[i] * 64,
                row[i + 1] * 16,
                row[i + 2] * 4,
                row[i + 3],
            ]))
        yield collapsed

def print_array(rows):
    print('[')
    for row in rows:
        row = [str(value).rjust(3, ' ') for value in row]
        print(f"    [{', '.join(row)}],")
    print(']')

if __name__ == '__main__':
    rows = [row for row in read_image()]
    color_map = create_color_map(rows)
    print(f"# Original colors: {color_map}")
    rows = [row for row in collapse_pixels(rows, color_map)]
    print_array(rows)
