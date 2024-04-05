#include <stdio.h>
#include <time.h>
#include <string.h>
#include <math.h>
#include "driver/gpio.h"
#include "sdkconfig.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#define swC 35
#define swD 34
#define swA 33
#define swB 32
#define keL 19
#define keU 18
#define keD 17
#define keR 16
gpio_num_t keys[] = {keL, keU, keD, keR, swC, swD, swA, swB};

void app_main(void)
{  
  printf("Ep.05 Keypad\n"); 
  for (int i=0; i<8; i++) {
    gpio_pad_select_gpio(keys[i]);
    gpio_pullup_en(keys[i]);
    if (gpio_set_direction(keys[i], GPIO_MODE_INPUT) == ESP_OK) {
      printf("GPIO%02d ... Success.\n",keys[i]);
    } else {
      printf("GPIO%02d ... Parameter error.\n",keys[i]);
    }
  }
  vTaskDelay( 1000/portTICK_PERIOD_MS );

  while(1) {
    printf("%d:%d:%d:%d %d-%d %d-%d\n",
      gpio_get_level(keys[0]),
      gpio_get_level(keys[1]),
      gpio_get_level(keys[2]),
      gpio_get_level(keys[3]),
      gpio_get_level(keys[4]),
      gpio_get_level(keys[5]),
      gpio_get_level(keys[6]),
      gpio_get_level(keys[7])
    );
    vTaskDelay( 100/portTICK_PERIOD_MS );
  }
}
