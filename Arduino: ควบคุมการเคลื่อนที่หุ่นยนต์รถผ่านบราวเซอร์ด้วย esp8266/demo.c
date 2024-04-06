#define MOTOR_L1  D4
#define MOTOR_L2  D5
#define MOTOR_R1  D6
#define MOTOR_R2  D7

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
      digitalWrite( MOTOR_L1, HIGH );
      digitalWrite( MOTOR_L2, LOW );
      digitalWrite( MOTOR_R1, LOW );
      digitalWrite( MOTOR_R2, HIGH );
    }
    void left() {
      digitalWrite( MOTOR_L1, HIGH );
      digitalWrite( MOTOR_L2, LOW );
      digitalWrite( MOTOR_R1, HIGH );
      digitalWrite( MOTOR_R2, LOW );
    }
    void right() {
      digitalWrite( MOTOR_L1, LOW );
      digitalWrite( MOTOR_L2, HIGH );
      digitalWrite( MOTOR_R1, LOW );
      digitalWrite( MOTOR_R2, HIGH );
    }
    void backward() {
      digitalWrite( MOTOR_L1, LOW );
      digitalWrite( MOTOR_L2, HIGH );
      digitalWrite( MOTOR_R1, HIGH );
      digitalWrite( MOTOR_R2, LOW );
    }
};

RobotAgent car;

void setup() {
}

void loop() {
  car.stop();
  car.forward();
  delay(3000);
  car.stop();
  car.backward();
  delay(3000);
  car.stop();
  car.left();
  delay(3000);
  car.stop();
  car.right();
  delay(3000);
}
