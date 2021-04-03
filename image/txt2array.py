#!/usr/bin/env python3

import fileinput
from typing import Dict, List


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
        cols.append(elements[2][1:])
    yield cols


def create_color_map(rows: List[List[str]]):
    colors = set()
    for row in rows:
        colors.update(row)
    if len(colors) != 4:
        print(f"Expected exactly 4 colors: {', '.join(colors)}.")
        exit(1)
    sorted_colors = sorted(colors)
    return {
        sorted_colors[0]: 0,
        sorted_colors[1]: 2,
        sorted_colors[2]: 3,
        sorted_colors[3]: 1,
    }


def collapse_pixels(rows: List[List[str]],
                    color_map: Dict[str, int]):
    for row_original in rows:
        row = [color_map[value] for value in row_original]
        collapsed = []
        for i in range(0, len(row), 4):
            collapsed.append(sum([
                row[i] * 64,
                row[i + 1] * 16,
                row[i + 2] * 4,
                row[i + 3],
            ]))
        yield collapsed


def print_array(rows: List[List[int]]):
    print(f"const unsigned char img_data[{len(rows[0])} * {len(rows)}] PROGMEM={{")
    for row in rows:
        row_formatted = [str(value).rjust(3, ' ') for value in row]
        print(f"  {','.join(row_formatted)},")
    print('};')


def _main():
    rows = [row for row in read_image()]
    color_map = create_color_map(rows)
    print(f"# Original colors: {color_map}")
    rows = [row for row in collapse_pixels(rows, color_map)]
    print_array(rows)


if __name__ == '__main__':
    _main()
