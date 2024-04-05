#include <stdio.h>
#include <time.h>
#include <string.h>
#include <math.h>
#include <sdkconfig.h>
#include <driver/gpio.h>
#include <driver/ledc.h>
#include <freertos/FreeRTOS.h>
#include <freertos/task.h>

#define pinSpk 26 
#define pinLED 23 

#define LEDC_DUTY_MAX   (8191)
#define LEDC_DUTY       (4095) // ปรับค่าดิวตี้เป็น 50% จาก (213-1)*50/100 จึงได้ค่าเป็น 4095

void testSpk() {
  // Speaker
  printf("Speaker ... C .. ");
  ledc_timer_config_t ledc_timer = {
        .speed_mode       = LEDC_LOW_SPEED_MODE,
        .timer_num        = LEDC_TIMER_0, 
        .duty_resolution  = LEDC_TIMER_13_BIT, // 213
        .freq_hz          = 262,
        .clk_cfg          = LEDC_AUTO_CLK
  };
  ledc_timer_config(&ledc_timer);

  ledc_channel_config_t ledc_channel = {
        .speed_mode     = LEDC_LOW_SPEED_MODE,
        .channel        = LEDC_CHANNEL_0,
        .timer_sel      = LEDC_TIMER_0,
        .intr_type      = LEDC_INTR_DISABLE,
        .gpio_num       = pinSpk,
        .duty           = 0, // Set duty to 0%
        .hpoint         = 0
  };
  ledc_channel_config(&ledc_channel);

  // สร้างความถี่ 262Hz
  ledc_set_duty(LEDC_LOW_SPEED_MODE, LEDC_CHANNEL_0, 262);
  ledc_update_duty(LEDC_LOW_SPEED_MODE, LEDC_CHANNEL_0);

 // หน่วงเวลา 2 วินาที
  vTaskDelay( 2000/portTICK_PERIOD_MS ); 

  printf("done.\n");

  // ปิดการทำงานของ LEDC หรือ PWM
  ledc_stop(LEDC_LOW_SPEED_MODE, LEDC_CHANNEL_0, 0);
}

void testLED() {
  // fade the LED
  printf("LED ... ");
  ledc_timer_config_t ledc_timer = {
        .speed_mode       = LEDC_LOW_SPEED_MODE,
        .timer_num        = LEDC_TIMER_1,
        .duty_resolution  = LEDC_TIMER_13_BIT,
        .freq_hz          = 50,  // Set output frequency at 5 kHz
        .clk_cfg          = LEDC_AUTO_CLK
  };
  ledc_timer_config(&ledc_timer);
  ledc_channel_config_t ledc_channel = {
        .speed_mode     = LEDC_LOW_SPEED_MODE,
        .channel        = LEDC_CHANNEL_1,
        .timer_sel      = LEDC_TIMER_1,
        .intr_type      = LEDC_INTR_DISABLE,
        .gpio_num       = pinLED,
        .duty           = 0, // Set duty to 100%
        .hpoint         = 0
  };
  ledc_channel_config(&ledc_channel);

  int i;
  // ปรับค่าดิวตี้เพื่อให้หลอดเปลี่ยนจากดับเป็นสว่าง
  for (i=200; i>0; i--) {
    ledc_set_duty(LEDC_LOW_SPEED_MODE, LEDC_CHANNEL_1,i*40);
    ledc_update_duty(LEDC_LOW_SPEED_MODE, LEDC_CHANNEL_1);
    // หน่วงเวลาเพื่อให้เห็นผลของการเปลี่ยน
    vTaskDelay( 50/portTICK_PERIOD_MS ); 
  }

  // เปล่ยนค่าดิวตี้เพื่อเปลี่ยนจากสว่างเป็นดับ
  for (i=0; i<200; i++) {
    ledc_set_duty(LEDC_LOW_SPEED_MODE, LEDC_CHANNEL_1,i*40);
    ledc_update_duty(LEDC_LOW_SPEED_MODE, LEDC_CHANNEL_1);
    // หน่วงเวลาเพื่อให้เห็นผลของการเปลี่ยน
    vTaskDelay( 50/portTICK_PERIOD_MS ); 
  }

  printf("done.\n");

  // ปิดการทำงานของ LEDC หรือ PWM
  ledc_stop(LEDC_LOW_SPEED_MODE, LEDC_CHANNEL_1, 1);
}

void app_main(void)
{
  printf("Ep.09 DAC\n"); 
  testSpk();
  testLED();
  printf("End of program\n");
}
