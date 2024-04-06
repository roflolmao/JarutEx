#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

#define AP_NAME "JarutEx"
#define AP_PASSWD "123456789"

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
IPAddress myIP(192, 168, 4, 1);
IPAddress gwIP(192, 168, 4, 10);
IPAddress subnet(255, 255, 255, 0);
int motionState = 0;

ESP8266WebServer server(80);

void setup() {
  motionState = 0;
  car.stop();
  if (WiFi.softAPConfig( myIP, gwIP, subnet )) {
    if (WiFi.softAP(AP_NAME, AP_PASSWD, 8, false, 5)) {
    } else {
      while (true);
    }
  } else {
    while (true) {
    }
  }
  server.on("/", htmlPage);
  server.on("/stop", robotStop);
  server.on("/forward", robotForward);
  server.on("/backward", robotBackward);
  server.on("/left", robotLeft);
  server.on("/right", robotRight);
  
  server.begin();
}

void robotStop() {
  motionState = 0;
  car.stop();
  htmlPage();
}
void robotForward() {
  motionState = 1;
  car.forward();
  htmlPage();
}
void robotBackward() {
  motionState = 2;
  car.backward();
  htmlPage();
}
void robotLeft(){ 
  motionState = 3;
  car.left();
  htmlPage();
}
void robotRight(){ 
  motionState = 4;
  car.right();
  htmlPage();
}

void htmlPage() {
  String html;
  html.reserve(2048);               // prevent ram fragmentation
  html = F(
           "<!DOCTYPE HTML>"
           "<html><head>"
           "<meta name='viewport' content='width=device-width, initial-scale=1'>"
           "<style>"

           ".button {  border: none;  color: white;  padding: 20px;  text-align: center;  text-decoration: none;"
           "  display: inline-block;  font-size: 14"
           "  px;  margin: 4px 2px;  cursor: pointer;  border-radius: 4%;"
           "  width: 100%; height: 100%;"
           "}"
           ".button1 {  background-color: #3ABC40; }"
           ".button2 {  background-color: #BC4040; }"
           "</style></head><body><table>"
         );
  if (motionState == 0) {
    html += F(
              "<tr>"
              "<td></td>"
              "<td><a href='/forward'><button class='button button2'>Forward</button></a></td>"
              "<td></td>"
              "</tr>"
              "<tr>"
              "<td><a href='/left'><button class='button button2'>Turn Left</button></a></td>"
              "<td><a href='/stop'><button  class='button button1'>Stop</button></a></td>"
              "<td><a href='/right'><button class='button button2'>Turn Right</button></a></td>"
              "</tr>"
              "<tr>"
              "<td></td>"
              "<td><a href='/backward'><button class='button button2'>Backward</button></a></td>"
              "<td></td>"
              "</tr>"
            );
  }
  else if (motionState == 1) {
    html += F(
              "<tr>"
              "<td></td>"
              "<td><a href='/forward'><button class='button button1'>Forward</button></a></td>"
              "<td></td>"
              "</tr>"
              "<tr>"
              "<td><a href='/left'><button class='button button2'>Turn Left</button></a></td>"
              "<td><a href='/stop'><button  class='button button2'>Stop</button></a></td>"
              "<td><a href='/right'><button class='button button2'>Turn Right</button></a></td>"
              "</tr>"
              "<tr>"
              "<td></td>"
              "<td><a href='/backward'><button class='button button2'>Backward</button></a></td>"
              "<td></td>"
              "</tr>"
            );

  }
  else if (motionState == 2) {
    html += F(
              "<tr>"
              "<td></td>"
              "<td><a href='/forward'><button class='button button2'>Forward</button></a></td>"
              "<td></td>"
              "</tr>"
              "<tr>"
              "<td><a href='/left'><button class='button button2'>Turn Left</button></a></td>"
              "<td><a href='/stop'><button  class='button button2'>Stop</button></a></td>"
              "<td><a href='/right'><button class='button button2'>Turn Right</button></a></td>"
              "</tr>"
              "<tr>"
              "<td></td>"
              "<td><a href='/backward'><button class='button button1'>Backward</button></a></td>"
              "<td></td>"
              "</tr>"
            );

  }
  else if (motionState == 3) {
    html += F(
              "<tr>"
              "<td></td>"
              "<td><a href='/forward'><button class='button button2'>Forward</button></a></td>"
              "<td></td>"
              "</tr>"
              "<tr>"
              "<td><a href='/left'><button class='button button1'>Turn Left</button></a></td>"
              "<td><a href='/stop'><button  class='button button2'>Stop</button></a></td>"
              "<td><a href='/right'><button class='button button2'>Turn Right</button></a></td>"
              "</tr>"
              "<tr>"
              "<td></td>"
              "<td><a href='/backward'><button class='button button2'>Backward</button></a></td>"
              "<td></td>"
              "</tr>"
            );

  }
  else if (motionState == 4) {
    html += F(
              "<tr>"
              "<td></td>"
              "<td><a href='/forward'><button class='button button2'>Forward</button></a></td>"
              "<td></td>"
              "</tr>"
              "<tr>"
              "<td><a href='/left'><button class='button button2'>Turn Left</button></a></td>"
              "<td><a href='/stop'><button  class='button button2'>Stop</button></a></td>"
              "<td><a href='/right'><button class='button button1'>Turn Right</button></a></td>"
              "</tr>"
              "<tr>"
              "<td></td>"
              "<td><a href='/backward'><button class='button button2'>Backward</button></a></td>"
              "<td></td>"
              "</tr>"
            );

  }
  html += F("</table></body></html>\r\n");
  server.send(200, "text/html", html);
}

void loop() {
  server.handleClient();
}
