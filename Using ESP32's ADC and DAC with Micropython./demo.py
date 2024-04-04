import time
from machine import ADC, DAC, Pin, TouchPad
adcPin1 = Pin(36) # ต่อกับขา 26 (dacPin2)
dacPin1 = Pin(25) # ต่อกับลำโพง
dacPin2 = Pin(26) # ต่อกับ adcPin1
swPin = Pin(16)

adc1 = ADC( adcPin1 )
adc1.width( ADC.WIDTH_12BIT ) # 12bit
adc1.atten( ADC.ATTN_11DB ) # 3.3V
dac1 = DAC( dacPin1 )
dac2 = DAC( dacPin2 )

# โปรแกรมหลัก
while True:
    # รอการกด TouchPad
    touched = swPin.value()
    if (touched):
        # สุ่มค่า DAC
        dac2.write(200)
        # ส่งไป ADC
        dValue1 = adc1.read()
        # แปลงออกลำโพง
        dac1.write( int(dValue1/4096*256 ) )
        # หน่วงเวลา
        #time.sleep_ms(100)
    else:
        # ปิดเสียง
        dac1.write( 0 )
