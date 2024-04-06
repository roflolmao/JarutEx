#pragma config OSC = HS 
#pragma config OSCS = ON
#pragma config PWRT = OFF 
#pragma config BOR = ON  
#pragma config BORV = 25 
#pragma config WDT = OFF  
#pragma config WDTPS = 128 
#pragma config STVR = ON 
#pragma config LVP = ON 
#pragma config CP0 = OFF 
#pragma config CP1 = OFF
#pragma config CP2 = OFF
#pragma config CP3 = OFF
#pragma config CPB = OFF
#pragma config CPD = OFF 
#pragma config WRT0 = OFF  
#pragma config WRT1 = OFF
#pragma config WRT2 = OFF  
#pragma config WRT3 = OFF   
#pragma config WRTC = OFF
#pragma config WRTB = OFF 
#pragma config WRTD = OFF   
#pragma config EBTR0 = OFF 
#pragma config EBTR1 = OFF 
#pragma config EBTR2 = OFF
#pragma config EBTR3 = OFF 
#pragma config EBTRB = OFF   

#include <xc.h>

#define _XTAL_FREQ 20000000 


unsigned char number_patterns[] = {
    0x3F,
    0x06,
    0x5B,
    0x4F,
    0x66,
    0x6D,
    0x7D,
    0x07,
    0x7F,
    0x6F
};


void setup() {
    TRISC = 0x00; // 0b00000000
    TRISD = 0x00; // 0b00000000
}

void loop() {
    for (int i=0; i<10; i++) {
        // disable
        PORTD = 0b00000000;
        // transfer
        PORTC = number_patterns[i];
        // enable
        PORTD = 0b00000001;
        // delay
        __delay_ms(1000);   
    }
}

void main(void) {
    setup();
    while (1) {
        loop();
    }
    return;
}
