#define MOTOR_L1  D2
#define MOTOR_L2  D3
#define MOTOR_R1  D4
#define MOTOR_R2  D5

class RobotAgent {
  private:
  public:
    RobotAgent() {
      // Actuator
      pinMode(MOTOR_L1, OUTPUT);
      pinMode(MOTOR_L2, OUTPUT);
      pinMode(MOTOR_R1, OUTPUT);
      pinMode(MOTOR_R2, OUTPUT);
    }
    ~RobotAgent() {

    }
    void stop() {
      digitalWrite( MOTOR_L1, LOW );
      digitalWrite( MOTOR_L2, LOW );
      digitalWrite( MOTOR_R1, LOW );
      digitalWrite( MOTOR_R2, LOW );
      delay(5);
      digitalWrite( MOTOR_L1, HIGH );
      digitalWrite( MOTOR_L2, HIGH );
      digitalWrite( MOTOR_R1, HIGH );
      digitalWrite( MOTOR_R2, HIGH );
      delay(100);
      digitalWrite( MOTOR_L1, LOW );
      digitalWrite( MOTOR_L2, LOW );
      digitalWrite( MOTOR_R1, LOW );
      digitalWrite( MOTOR_R2, LOW );
    }
    void forward() {
      digitalWrite( MOTOR_L1, LOW );
      digitalWrite( MOTOR_L2, HIGH );
      digitalWrite( MOTOR_R1, HIGH );
      digitalWrite( MOTOR_R2, LOW );
    }
    void left() {
      digitalWrite( MOTOR_L1, LOW );
      digitalWrite( MOTOR_L2, HIGH );
      digitalWrite( MOTOR_R1, LOW );
      digitalWrite( MOTOR_R2, HIGH );

    }
    void right() {

      digitalWrite( MOTOR_L1, HIGH );
      digitalWrite( MOTOR_L2, LOW );
      digitalWrite( MOTOR_R1, HIGH );
      digitalWrite( MOTOR_R2, LOW );
    }
    void backward() {

      digitalWrite( MOTOR_L1, HIGH );
      digitalWrite( MOTOR_L2, LOW );
      digitalWrite( MOTOR_R1, LOW );
      digitalWrite( MOTOR_R2, HIGH );
    }
};

RobotAgent car;
int cmd;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    cmd = (int)Serial.read() - '0';
    switch (cmd) {
      case 0:
        car.stop();
        break;
      case 1:
        car.forward();
        break;
      case 2:
        car.backward();
        break;
      case 3:
        car.left();
        break;
      case 4:
        car.right();
        break;
    }
  }
}
