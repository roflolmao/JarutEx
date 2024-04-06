#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

#define AP_NAME "JarutEx"
#define AP_PASSWD "123456789"

IPAddress myIP(192, 168, 4, 1);
IPAddress gwIP(192, 168, 4, 10);
IPAddress subnet(255, 255, 255, 0);

int motionState = 0;
String html;

ESP8266WebServer server(80);


void setup() {
  Serial.begin(9600);
  delay(1000);
  html.reserve(2048);               // prevent ram fragmentation
  motionState = 0;
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
  Serial.println(motionState);
  htmlPage();
}
void robotForward() {
  motionState = 1;
  Serial.println(motionState);
  htmlPage();
}
void robotBackward() {
  motionState = 2;
  Serial.println(motionState);
  htmlPage();
}
void robotLeft() {
  motionState = 3;
  Serial.println(motionState);
  htmlPage();
}
void robotRight() {
  motionState = 4;
  Serial.println(motionState);
  htmlPage();
}

void htmlPage() {
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
