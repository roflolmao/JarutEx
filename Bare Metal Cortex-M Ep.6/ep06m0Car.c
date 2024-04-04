/* ep06m0Car -------------------------------------------------------------------
 * (C) 2021, JarutEx
 * https://www.jarutex.com
 * -----------------------------------------------------------------------------*/
#include "main.h"
#include <string.h>
#include <stdio.h>

UART_HandleTypeDef huart1;

void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_USART1_UART_Init(void);

void moveStop() {
	HAL_UART_Transmit(&huart1, (uint8_t*)"Stop\n",5,100);
	HAL_GPIO_WritePin(GPIOA, MOTOR_R1_Pin|MOTOR_R2_Pin|MOTOR_L1_Pin|MOTOR_L2_Pin, GPIO_PIN_SET);
}

void moveForward() {
	HAL_UART_Transmit(&huart1, (uint8_t*)"Forward\n",8,100);
	// Right
	HAL_GPIO_WritePin(GPIOA, MOTOR_R1_Pin, GPIO_PIN_SET);
	HAL_GPIO_WritePin(GPIOA, MOTOR_R2_Pin, GPIO_PIN_RESET);

	// Left
	HAL_GPIO_WritePin(GPIOA, MOTOR_L1_Pin, GPIO_PIN_RESET);
	HAL_GPIO_WritePin(GPIOA, MOTOR_L2_Pin, GPIO_PIN_SET);
}

void moveBackward() {
	HAL_UART_Transmit(&huart1, (uint8_t*)"Backward\n",9,100);
	// Right
	HAL_GPIO_WritePin(GPIOA, MOTOR_R1_Pin, GPIO_PIN_RESET);
	HAL_GPIO_WritePin(GPIOA, MOTOR_R2_Pin, GPIO_PIN_SET);

	// Left
	HAL_GPIO_WritePin(GPIOA, MOTOR_L1_Pin, GPIO_PIN_SET);
	HAL_GPIO_WritePin(GPIOA, MOTOR_L2_Pin, GPIO_PIN_RESET);
}

void turnLeft() {
	HAL_UART_Transmit(&huart1, (uint8_t*)"Turn Left\n",10,100);
	// Right
	HAL_GPIO_WritePin(GPIOA, MOTOR_R1_Pin, GPIO_PIN_RESET);
	HAL_GPIO_WritePin(GPIOA, MOTOR_R2_Pin, GPIO_PIN_SET);

	// Left
	HAL_GPIO_WritePin(GPIOA, MOTOR_L1_Pin, GPIO_PIN_RESET);
	HAL_GPIO_WritePin(GPIOA, MOTOR_L2_Pin, GPIO_PIN_SET);
}

void turnRight() {
	HAL_UART_Transmit(&huart1, (uint8_t*)"Turn Right\n",11,100);
	// Right
	HAL_GPIO_WritePin(GPIOA, MOTOR_R1_Pin, GPIO_PIN_SET);
	HAL_GPIO_WritePin(GPIOA, MOTOR_R2_Pin, GPIO_PIN_RESET);

	// Left
	HAL_GPIO_WritePin(GPIOA, MOTOR_L1_Pin, GPIO_PIN_SET);
	HAL_GPIO_WritePin(GPIOA, MOTOR_L2_Pin, GPIO_PIN_RESET);
}

int main(void)
{
  HAL_Init();
  SystemClock_Config();
  MX_GPIO_Init();
  MX_USART1_UART_Init();

  while (1)
  {
	  moveStop();
	  moveForward();
	  HAL_Delay(2000);
	  moveStop();
	  turnLeft();
	  HAL_Delay(2000);
	  moveStop();
	  moveBackward();
	  HAL_Delay(2000);
	  moveStop();
	  turnRight();
	  HAL_Delay(2000);
  }
}

void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};
  RCC_PeriphCLKInitTypeDef PeriphClkInit = {0};

  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_ON;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLMUL = RCC_PLL_MUL6;
  RCC_OscInitStruct.PLL.PREDIV = RCC_PREDIV_DIV1;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_1) != HAL_OK)
  {
    Error_Handler();
  }
  PeriphClkInit.PeriphClockSelection = RCC_PERIPHCLK_USART1;
  PeriphClkInit.Usart1ClockSelection = RCC_USART1CLKSOURCE_PCLK1;
  if (HAL_RCCEx_PeriphCLKConfig(&PeriphClkInit) != HAL_OK)
  {
    Error_Handler();
  }
}

static void MX_USART1_UART_Init(void)
{
  huart1.Instance = USART1;
  huart1.Init.BaudRate = 38400;
  huart1.Init.WordLength = UART_WORDLENGTH_8B;
  huart1.Init.StopBits = UART_STOPBITS_1;
  huart1.Init.Parity = UART_PARITY_NONE;
  huart1.Init.Mode = UART_MODE_TX_RX;
  huart1.Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart1.Init.OverSampling = UART_OVERSAMPLING_16;
  huart1.Init.OneBitSampling = UART_ONE_BIT_SAMPLE_DISABLE;
  huart1.AdvancedInit.AdvFeatureInit = UART_ADVFEATURE_NO_INIT;
  if (HAL_MultiProcessor_Init(&huart1, 0, UART_WAKEUPMETHOD_IDLELINE) != HAL_OK)
  {
    Error_Handler();
  }
}

static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};

  __HAL_RCC_GPIOF_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();

  HAL_GPIO_WritePin(GPIOA, MOTOR_R1_Pin|MOTOR_R2_Pin|MOTOR_L1_Pin|MOTOR_L2_Pin, GPIO_PIN_RESET);

  GPIO_InitStruct.Pin = MOTOR_R1_Pin|MOTOR_R2_Pin|MOTOR_L1_Pin|MOTOR_L2_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

}

void Error_Handler(void)
{
  __disable_irq();
  while (1)
  {
  }
}
