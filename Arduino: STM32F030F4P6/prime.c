#include <miniSerial.h>
#include <math.h>

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
  Serial.begin(9600);
  testPrimeNumber(2000);
  Serial.print("Found ");
  Serial.print(counter, DEC);
  Serial.print(" in ");
  Serial.print(int(fabs(t1 - t0)), DEC);
  Serial.println(" milliseconds.");
}
void loop(void)
{
}
