#include <VGAX.h>
#include <VGAXUtils.h>

VGAX vga;

void setup() {
  vga.begin(false);
}

void loop() {
  draw_house();
  vga.delay(4000);
  vga.clear(0);
  vga.delay(1000);
}

void line(uint8_t x0, uint8_t y0, uint8_t x1, uint8_t y1) {
  VGAXUtils::draw_line(x0,  y0, x1, y1, 2);
  vga.delay(1000);
}

void draw_house() {
  uint8_t eaves_width = 4;

  uint8_t x_left          = 0;
  uint8_t x_right         = 119;
  uint8_t x_wall_left     = x_left + eaves_width;
  uint8_t x_wall_right    = x_right - eaves_width;
  uint8_t x_mid           = (x_right - x_left) / 2;
  uint8_t x_chimney_left  = x_mid / 3;
  uint8_t x_chimney_right = x_chimney_left * 2;

  uint8_t y_roof           = 20;
  uint8_t y_top            = 0;
  uint8_t y_ground         = 59;
  uint8_t y_chimney_top    = 3;
  uint8_t y_chimney_down_l = 13;
  uint8_t y_chimney_down_r = 8;

  line(x_wall_left,  y_ground, x_wall_left,  y_roof);
  line(x_wall_right, y_ground, x_wall_right, y_roof);
  line(x_left,       y_roof,   x_right,      y_roof);
  line(x_left,       y_roof,   x_mid,        y_top);
  line(x_right,      y_roof,   x_mid,        y_top);
  
  line(x_chimney_left,  y_chimney_top,    x_chimney_right, y_chimney_top);
  line(x_chimney_left,  y_chimney_down_l, x_chimney_left,  y_chimney_top);
  //line(x_chimney_right, y_chimney_down_r, x_chimney_right, y_chimney_top);
}
