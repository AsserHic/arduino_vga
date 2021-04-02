#!/bin/bash

set -e

OUTPUT_BITMAP=output.png

if [ -z "$1" ]
  then
    echo "syntax: $0 input_image"
    exit 1
fi

echo "Converting $1 to an array..."
convert $1 -resize 120x60\! -depth 2 -colors 4 $OUTPUT_BITMAP
convert $OUTPUT_BITMAP txt:- | ./txt2array.py
