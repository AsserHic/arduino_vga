#!/usr/bin/env python3

import fileinput


def read_image():
    row = -1
    cols = []
    for line in fileinput.input():
        if row < 0:
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
    ordered_colors = sorted(colors)
    return {
       ordered_colors[0]: 1,
       ordered_colors[1]: 3,
       ordered_colors[2]: 2,
       ordered_colors[3]: 0,
    }

def collapse_pixels(rows, color_map):
    for row in rows:
        row = [color_map[value] for value in row]
        collapsed = []
        for i in range(0, len(row), 4):
            chunk = row[i:i + 4]
            collapsed.append(sum(chunk))
        yield collapsed

if __name__ == '__main__':
    rows = [row for row in read_image()]
    color_map = create_color_map(rows)
    rows = [row for row in collapse_pixels(rows, color_map)]
    print(rows)
