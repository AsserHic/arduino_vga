#include <Arduino.h>
#include <VGAX.h>
#include <VGAXUtils.h>

const int PIN_X = A1;
const int PIN_Y = A2;

const int BUFFER_LENGTH = 80;
uint8_t xBuffer[BUFFER_LENGTH];
uint8_t yBuffer[BUFFER_LENGTH];
int bufferPos = 0;

int limitsX[] = {400, 600};
int limitsY[] = {400, 600};

VGAX vga;

void setup() {
  pinMode(PIN_X, INPUT);
  pinMode(PIN_Y, INPUT);

  // Initialize buffer
  for (int i = 0; i < BUFFER_LENGTH; i++) {
      xBuffer[i] = yBuffer[i] = 0;
  }

  vga.begin(false);
  vga.clear(0);
}

void loop() {
  if (measureSignal()) {
    plotBuffer();
  }
}

boolean measureSignal() {
  int signalX = analogRead(PIN_X);
  int signalY = analogRead(PIN_Y);
  int valueX;
  int valueY;

  limitsX[0] = min(limitsX[0], signalX);
  limitsX[1] = max(limitsX[1], signalX);
  limitsY[0] = min(limitsY[0], signalY);
  limitsY[1] = max(limitsY[1], signalY);

  valueX  = map(signalX, limitsX[0], limitsX[1], 0, 119);
  valueY  = map(signalY, limitsY[0], limitsY[1], 0, 59);

  if (xBuffer[bufferPos] != valueX || yBuffer[bufferPos] != valueY) {
    bufferPos = (bufferPos + 1) % BUFFER_LENGTH;
    xBuffer[bufferPos] = valueX;
    yBuffer[bufferPos] = valueY;
    return true;
  }
  return false;
}

void plotBuffer() {
  int bufferLast = (bufferPos + 1) % BUFFER_LENGTH;

  vga.putpixel(xBuffer[bufferLast], yBuffer[bufferLast], 0);
  vga.putpixel(xBuffer[bufferPos],  yBuffer[bufferPos],  2);
}

