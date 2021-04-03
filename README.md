# arduino_vga

Video Graphics Array (VGA) tests for Arduino. These small applications are
inspired by [VGAX library](https://github.com/smaffer/vgax) and I've followed
the circuit schematics explained on its repository.

## house

Draws a simple green line house line by line.


## image

Renders a static four color image to the screen.

You can convert images to suitable arrays using bitmap2array script
(requires: ImageMagick & Python):

```sh
./bitmap2array.sh your_original.jpeg
```

The script will print the corresponding array to the standard output stream
and you may incorporate it to you code.


## xy_mode

A simple prototype of a low-frequency voltage view for two analog input pins.
The current voltage of the both channels is represented as a dot on the screen
so that the horizontal axis represents pin A1 and the vertical axis represents
pin A2. A small buffer is used for a short tail following the latest
measurement.
