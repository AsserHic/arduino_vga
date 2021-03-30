#include <VGAX.h>
#include <VGAXUtils.h>

VGAX vga;

void setup() {
  vga.begin();
}

void loop() {
  draw_house();
  
}

void draw_house() {
  unsigned int x_left      = 0;
  unsigned int x_right     = 29;
  unsigned int x_wall_left = x_left + eaves_width;
  unsigned int x_mid       = (X_RIGHT - X_LEFT) / 2;
  
  unsigned int y_top       = 0;
  unsigned int y_ground    = 59;

  VGAXUtils::draw_line(x_wall_left,  y_ground, x_wall_left,  Y_ROOF);
  VGAXUtils::draw_line(x_wall_right, y_ground, X_WALL_RIGHT, Y_ROOF);
  VGAXUtils::draw_line(x_left,       Y_ROOF,   x_right,      Y_ROOF);
  VGAXUtils::draw_line(x_left,       Y_ROOF,   X_MID,        Y_TOP);
  VGAXUtils::draw_line(x_right,      Y_ROOF,   X_MID,        Y_TOP);
}
