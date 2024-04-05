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

void app_main(void)
{  
  dac_cw_config_t cwCfg;

  cwCfg.en_ch = pinDAC;
  cwCfg.scale = DAC_CW_SCALE_1;
  cwCfg.phase = DAC_CW_PHASE_180;
  cwCfg.freq = 262; // 262Hz
  cwCfg.offset = 127;

  printf("Ep.08 DAC\n"); 
  dac_i2s_enable();
  dac_i2s_disable();
  if (dac_cw_generator_config(&cwCfg) == ESP_OK) {
    printf("Start cosine-wave generator ...");
    dac_cw_generator_enable();
    dac_output_enable( pinDAC );
    vTaskDelay( 2000/portTICK_PERIOD_MS ); // 2 seconds
    dac_cw_generator_disable();
    dac_output_disable( pinDAC );
    printf("done.\n");
  } else {
    printf("Error : ESP_ERR_INVALID_ARG!\n");
  }
  while (1) {
    vTaskDelay( 10/portTICK_PERIOD_MS ); 
  }
}
