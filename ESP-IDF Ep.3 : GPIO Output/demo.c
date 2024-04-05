#include <stdio.h>
#include <time.h>
#include <string.h>
#include <math.h>
#include "driver/gpio.h"
#include "sdkconfig.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#define LED_PIN 13 // GPIO13

void app_main(void)
{  
  printf("Ep.02 GPIO"); 
  gpio_pad_select_gpio(LED_PIN);
  gpio_set_direction(LED_PIN, GPIO_MODE_OUTPUT);

  while(1) {
    gpio_set_level(LED_PIN, 0);
    vTaskDelay( 500/portTICK_PERIOD_MS );
    gpio_set_level(LED_PIN, 1 );
    vTaskDelay( 500/portTICK_PERIOD_MS );
  }
}
