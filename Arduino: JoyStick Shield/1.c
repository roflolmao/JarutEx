/****************************************************************
   Joypad Shield
   by JarutEx (https://www.jarutex.com)
 ****************************************************************/
#define VR_X 0
#define VR_Y 1
#define VR_SW 8
#define SW_SELECT 7 // Select
#define SW_START 6 // Start
#define SW_X 5 // blue left
#define SW_Y 2 // yellow top
#define SW_A 4 // yellow bottom
#define SW_B 3 // blue right
#define NUM_SWITCHES 7

uint8_t swPins[NUM_SWITCHES] = {VR_SW, SW_SELECT, SW_START, SW_X, SW_Y, SW_A, SW_B};
uint8_t swStatus[NUM_SWITCHES] = {0, 0, 0, 0, 0, 0, 0}; // 1-pressed, 0-released
uint16_t joy[2] = {0, 0}; // x,y

void doInput() {
  joy[0] = analogRead(0);
  joy[1] = analogRead(1);
  for (int i = 0; i < NUM_SWITCHES; i++) {
    swStatus[i] = ((digitalRead(swPins[i])) ? (0) : (1));
  }
}

void doShowInfo() {
  Serial.print("X: ");
  Serial.print(joy[0]);
  Serial.print(" Y: ");
  Serial.print(joy[1]);
  Serial.print(" Sw: ");
  for (int i = 0; i < NUM_SWITCHES; i++) {
    Serial.print(swStatus[i]);
    if (i < (NUM_SWITCHES - 1)) {
      Serial.print(":");
    }
  }
  Serial.println();
}

void setup() {
  Serial.begin(115200);
  for (int i = 0; i < NUM_SWITCHES; i++) {
    pinMode( swPins[i], INPUT );
    digitalWrite( swPins[i], HIGH );
  }
}

void loop() {
  doInput();
  doShowInfo();
}
