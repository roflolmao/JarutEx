#include <stdio.h>
#include <time.h>
#include <string.h>
#include <math.h>
#include <sdkconfig.h>
#include <driver/gpio.h>
#include <driver/dac.h>
#include <driver/dac_common.h>
#include <freertos/FreeRTOS.h>
#include <freertos/task.h>

#define pinDAC DAC_CHANNEL_2

void wave1() {
  int dValue=0;
  printf("Start wave1 ...");
  dac_output_enable( pinDAC );
  while (true) {
    dac_output_voltage( pinDAC, dValue++ );
    vTaskDelay( 10/portTICK_PERIOD_MS );
    if (dValue > 255) {
        break;
    }
  }
  dac_output_disable( pinDAC );
  printf("done.\n");
}

void app_main(void)
{  
  printf("Ep.07 DAC\n"); 
  dac_i2s_enable();
  dac_i2s_disable();

  while(1) {
    wave1();
    vTaskDelay( 10/portTICK_PERIOD_MS );
  }
}
