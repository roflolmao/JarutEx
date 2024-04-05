uint32_t counter = 0;
uint32_t t0, t1;
uint32_t t2000;

uint32_t isPrimeNumber(uint32_t x) {
  uint32_t i;
  for (i = 2; i < x; i++) {
    if (x % i == 0) {
      return 0;
    }
  }
  if (i == x)
    return 1;
  return 0;
}


void testPrimeNumber(uint32_t maxN) {
  counter = 0;
  t0 = millis();
  for (uint32_t n = 2; n < maxN; n++) {
    if (isPrimeNumber(n)) {
      counter++;
    }
  }
  t1 = millis();
}


void setup() {
  SerialUSB.begin(115200);
  SerialUSB.println();
}

void loop() {
  testPrimeNumber(2000);
  SerialUSB.print("\n\nTest 2,000 times : Found ");
  SerialUSB.print(counter, DEC);
  SerialUSB.print(" in ");
  t2000 = int(fabs(t1 - t0));
  SerialUSB.print(t2000, DEC);
  SerialUSB.println(" milliseconds.");
  delay(15000);
}
