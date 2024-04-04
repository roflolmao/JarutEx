int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_USART1_UART_Init();
  /* USER CODE BEGIN 2 */
  char msg[32];
  int msgLen=0;

  sprintf(msg,"...Say something...\n");
  msgLen = strlen( msg );
  HAL_UART_Transmit( &huart1, (uint8_t*)msg, msgLen, 100);

  strcpy(msg,"");
  HAL_UART_Receive(  &huart1, (uint8_t*)msg, 32, 5000 );
  for (int i=0; i<32; i++) {
	  if (msg[i] == '\n') {
		  msg[i] = 0;
		  break;
	  }
	  if (msg[i] == '\r') {
		  msg[i] = 0;
		  break;
	  }
  }
  msgLen = strlen( msg );
  HAL_UART_Transmit( &huart1, (uint8_t*)msg, msgLen, 100);
  HAL_UART_Transmit( &huart1, (uint8_t*)"\nEnd of program.\n", 17, 100);
  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
  }
}
