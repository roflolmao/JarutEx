#include <stdio.h>
#include <time.h>
#include <string.h>
#include <math.h>

#include "sdkconfig.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_system.h"
#include "esp_spi_flash.h"

int counter = 0;
float t0, t1;

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

void testPrimeNumber(uint16_t maxN) {
  t0 = esp_timer_get_time()/1000.0;
  for (uint16_t n = 2; n < maxN; n++) {
    if (isPrimeNumber(n)) {
      counter++;
    }
  }
  t1 = esp_timer_get_time()/1000.0;
}

void app_main(void)
{  
    testPrimeNumber(2000);
    printf("Found %d in %f milliseconds.\n", counter, fabs(t1-t0)); 
}
