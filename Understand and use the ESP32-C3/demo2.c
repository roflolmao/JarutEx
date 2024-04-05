#include <stdio.h>
#include <time.h>
#include <string.h>
#include <math.h>
#include "driver/gpio.h"
#include "sdkconfig.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#define LED_R_PIN 3
#define LED_G_PIN 4
#define LED_B_PIN 5

void app_main(void)
{  
  printf("C3 LEDs"); 
  gpio_pad_select_gpio(LED_R_PIN);
  gpio_set_direction(LED_R_PIN, GPIO_MODE_OUTPUT);
  gpio_pad_select_gpio(LED_G_PIN);
  gpio_set_direction(LED_G_PIN, GPIO_MODE_OUTPUT);
  gpio_pad_select_gpio(LED_B_PIN);
  gpio_set_direction(LED_B_PIN, GPIO_MODE_OUTPUT);

  while(1) {
    gpio_set_level(LED_R_PIN, 1);
    vTaskDelay( 500/portTICK_PERIOD_MS );
    gpio_set_level(LED_R_PIN, 0 );
    vTaskDelay( 500/portTICK_PERIOD_MS );
    gpio_set_level(LED_G_PIN, 1);
    vTaskDelay( 500/portTICK_PERIOD_MS );
    gpio_set_level(LED_G_PIN, 0 );
    vTaskDelay( 500/portTICK_PERIOD_MS );
    gpio_set_level(LED_B_PIN, 1);
    vTaskDelay( 500/portTICK_PERIOD_MS );
    gpio_set_level(LED_B_PIN, 0 );
    vTaskDelay( 500/portTICK_PERIOD_MS );
    gpio_set_level(LED_R_PIN, 1 );
    gpio_set_level(LED_G_PIN, 1 );
    gpio_set_level(LED_B_PIN, 0 );
    vTaskDelay( 500/portTICK_PERIOD_MS );
    gpio_set_level(LED_R_PIN, 0 );
    gpio_set_level(LED_G_PIN, 1 );
    gpio_set_level(LED_B_PIN, 1 );
    vTaskDelay( 500/portTICK_PERIOD_MS );
    gpio_set_level(LED_R_PIN, 1 );
    gpio_set_level(LED_G_PIN, 0 );
    gpio_set_level(LED_B_PIN, 1 );
    vTaskDelay( 500/portTICK_PERIOD_MS );
    gpio_set_level(LED_R_PIN, 1 );
    gpio_set_level(LED_G_PIN, 1 );
    gpio_set_level(LED_B_PIN, 1 );
    vTaskDelay( 500/portTICK_PERIOD_MS );
    gpio_set_level(LED_R_PIN, 0 );
    gpio_set_level(LED_G_PIN, 0 );
    gpio_set_level(LED_B_PIN, 0 );
    vTaskDelay( 500/portTICK_PERIOD_MS );
  }
}
