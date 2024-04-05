#include <stdio.h>
#include <time.h>
#include <string.h>
#include <math.h>
#include <driver/adc.h>
#include "driver/gpio.h"
#include "sdkconfig.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#define pinADC ADC1_CHANNEL_0 // GPIO36

float dValueToVolt( int dValue ) 
{
    return (float)((dValue/4096.0f)*3.3f);
}

void app_main(void)
{  
  int dValue = 0;
  float volt = 0.0;

  printf("Ep.06 ADC\n"); 
  adc1_config_width( ADC_WIDTH_BIT_12 );
  adc1_config_channel_atten( pinADC, ADC_ATTEN_DB_11);

  while(1) {
    dValue = adc1_get_raw( pinADC );
    volt = dValueToVolt( dValue );
    printf("dValue = %d, V = %.2f\n",
      dValue, volt);
    vTaskDelay( 250/portTICK_PERIOD_MS );
  }
}
