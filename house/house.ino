#include <VGAX.h>
#include <VGAXUtils.h>

#define GREEN  2
#define YELLOW 3

VGAX vga;

void setup() {
  vga.begin(false);
}

void loop() {
  drawHouse();
  vga.delay(2000);
  turnLightsOn();
  vga.delay(2000);
  vga.clear(0);
  vga.delay(1000);
}

void line(uint8_t x0, uint8_t y0, uint8_t x1, uint8_t y1) {
  VGAXUtils::draw_line(x0,  y0, x1, y1, GREEN);
  vga.delay(800);
}

void drawHouse() {
  uint8_t door_width    = 17;
  uint8_t eaves_width   = 8;
  uint8_t window_height = 10;
  uint8_t window_width  = 23;

  uint8_t x_left          = 0;
  uint8_t x_right         = 119;
  uint8_t x_wall_left     = x_left + eaves_width;
  uint8_t x_wall_right    = x_right - eaves_width;
  uint8_t x_mid           = (x_right - x_left) / 2;
  uint8_t x_chimney_left  = x_mid / 3;
  uint8_t x_chimney_right = x_chimney_left * 2;
  uint8_t x_door_right    = x_wall_right - door_width;
  uint8_t x_door_left     = x_door_right - door_width;

  uint8_t y_roof           = 20;
  uint8_t y_top            = 0;
  uint8_t y_ground         = 59;
  uint8_t y_chimney_top    = 3;
  uint8_t y_chimney_down_l = 13;
  uint8_t y_chimney_down_r = 8;
  uint8_t y_door_top       = 42;
  uint8_t y_door_lock      = (y_ground + y_door_top) / 2;

  line(x_wall_left,  y_ground, x_wall_left,  y_roof);
  line(x_wall_right, y_ground, x_wall_right, y_roof);
  line(x_left,       y_roof,   x_right,      y_roof);
  line(x_left,       y_roof,   x_mid,        y_top);
  line(x_right,      y_roof,   x_mid,        y_top);
  
  line(x_chimney_left,  y_chimney_top,    x_chimney_right, y_chimney_top);
  line(x_chimney_left,  y_chimney_down_l, x_chimney_left,  y_chimney_top);
  line(x_chimney_right, y_chimney_down_r, x_chimney_right, y_chimney_top);

  line(x_door_left,  y_ground,    x_door_left,      y_door_top);
  line(x_door_right, y_ground,    x_door_right,     y_door_top);
  line(x_door_left,  y_door_top,  x_door_right,     y_door_top);
  line(x_door_right, y_door_lock, x_door_right - 3, y_door_lock);

  drawWindow(x_chimney_left, y_roof + 5, window_height, window_width);
  drawWindow(x_mid,          y_roof + 5, window_height, window_width);
}

void drawWindow(uint8_t x_left, uint8_t y_top, uint8_t height, uint8_t width) {
  uint8_t x_right = x_left + width;
  uint8_t x_mid   = (x_left + x_right) / 2;
  uint8_t y_down  = y_top + height;

  line(x_left,  y_down, x_left,  y_top);
  line(x_left,  y_down, x_right, y_down);
  line(x_left,  y_top,  x_right, y_top);
  line(x_right, y_down, x_right, y_top);
  line(x_mid,   y_down, x_mid,   y_top);
}

void turnLightsOn() {
  VGAXUtils::draw_rect(20, 26, 9, 8, YELLOW, YELLOW);
  vga.putpixel(29, 34, YELLOW);
  VGAXUtils::draw_rect(31, 26, 10, 8, YELLOW, YELLOW);
  vga.putpixel(41, 34, YELLOW);
}
