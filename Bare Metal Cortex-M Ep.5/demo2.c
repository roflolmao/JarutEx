int main(void)
{
  uint16_t dValue[10];
  uint8_t dIndex=0;
  uint32_t dSum = 0;
  uint32_t dAverage=0;
  uint16_t dMin=4096, dMax=0;
  char msg[32]="";
  uint8_t msgLen;

  HAL_Init();

  SystemClock_Config();

  MX_GPIO_Init();
  MX_ADC_Init();
  MX_USART1_UART_Init();
  HAL_ADCEx_Calibration_Start(&hadc);

  while (1)
  {
		HAL_ADC_Start(&hadc);
		HAL_ADC_PollForConversion(&hadc, 1); // อ่าน 1ms
		dValue[dIndex] = HAL_ADC_GetValue(&hadc);
		dSum += dValue[dIndex];
		if (dValue[dIndex]>dMax){
			dMax = dValue[dIndex];
		}
		if (dValue[dIndex]<dMin) {
			dMin = dValue[dIndex];
		}
		dIndex++;
		if (dIndex == 10) {
			dAverage = (uint32_t)(dSum/10);
			dSum = 0;
			dIndex = 0;
			sprintf(msg,"Min=%d, Max=%d, Average=%ld\n", dMin,dMax,dAverage);
			msgLen = strlen( msg );
			HAL_UART_Transmit( &huart1, (uint8_t*)msg, msgLen, 100);
		}
		HAL_Delay(5);
  }
}
