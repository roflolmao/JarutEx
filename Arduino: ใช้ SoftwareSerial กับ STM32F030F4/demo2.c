#include <math.h>
#include <SoftwareSerial.h>

SoftwareSerial mySerial(PA10, PA9);
#define PIN_LED PA4

bool isPrimeNumber(uint16_t x) {
  uint16_t i;
  for (i = 2; i < x; i++) {
    if (x % i == 0) {
      return false;
    }
  }
  if (i == x)
    return true;
  return false;
}

int counter = 0;
uint32_t t0, t1;

void testPrimeNumber(uint16_t maxN) {
  t0 = millis();
  for (uint16_t n = 2; n < maxN; n++) {
    if (isPrimeNumber(n)) {
      counter++;
    }
  }
  t1 = millis();
}

void setup(void)
{
  pinMode( PIN_LED, OUTPUT );
  mySerial.begin(9600);
  testPrimeNumber(2000);
  mySerial.print("Found ");
  mySerial.print(counter, DEC);
  mySerial.print(" in ");
  mySerial.print(int(fabs(t1 - t0)), DEC);
  mySerial.println(" milliseconds.");
}
void loop(void)
{
  digitalWrite( PIN_LED, HIGH );
  delay(500);
  digitalWrite( PIN_LED, LOW );
  delay(500);
}
