// Relay 5V
#define relayPin 0
#define ledPin 2

void setup() {
  pinMode( relayPin, OUTPUT );
  pinMode( ledPin, OUTPUT );
}

void loop() {
  digitalWrite( ledPin, HIGH ); 
  digitalWrite( relayPin, HIGH );
  delay(10000);
  digitalWrite( ledPin, LOW ); 
  digitalWrite( relayPin, LOW );
  delay(10000);
}
