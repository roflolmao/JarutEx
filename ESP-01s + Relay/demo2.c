// control Relay
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

#define AP_NAME "JarutEx"
#define AP_PASSWD "123456789"
#define relayPin 0
#define ledPin 2

IPAddress myIP(192, 168, 4, 1);
IPAddress gwIP(192, 168, 4, 10);
IPAddress subnet(255, 255, 255, 0);

ESP8266WebServer server(80);


void setup() {
  pinMode( relayPin, OUTPUT );
  pinMode( ledPin, OUTPUT );
  if (WiFi.softAPConfig( myIP, gwIP, subnet )) {
    if (WiFi.softAP(AP_NAME, AP_PASSWD, 8, false, 5)) {
      digitalWrite( ledPin, HIGH );
    } else {
      digitalWrite( ledPin, LOW );
      while (true);
    }
  } else {
    while (true) {
      digitalWrite( ledPin, LOW );
      delay(100);
      digitalWrite( ledPin, HIGH );
      delay(100);
    }
  }
  server.on("/", htmlPage);
  server.on("/turnOn", doTurnOn);
  server.on("/turnOff", doTurnOff);
  server.begin();
}

int relayStatus = 0; // 0 = off, 1 = on


void doTurnOn() {
  relayStatus = 1;
  digitalWrite( relayPin, LOW );

  htmlPage();
}

void doTurnOff() {
  relayStatus = 0;
  digitalWrite( relayPin, HIGH );
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
           "html {font-family: Arial; display: inline-block; text-align: center;}"
           "h1 {font-size: 3.0rem;}"
           "p {font-size: 3.0rem;}"
           "body {max-width: 800px; margin:0px auto; padding-bottom: 16px;}"
           ".switch {position: relative; display: inline-block; width: 120px; height: 68px} "
           ".switch input {display: none}"
           ".slider {position: absolute; top: 0; left: 0; right: 0; bottom: 0; background-color: #ccc; border-radius: 34px}"
           ".slider:before {position: absolute; content: ''; height: 52px; width: 52px; left: 8px; bottom: 8px; background-color: #fff; -webkit-transition: .4s; transition: .4s; border-radius: 68px}"
           "input:checked+.slider {background-color: #2196F3}"
           "input: checked+.slider:before {-webkit-transform: translateX(52px); -ms-transform: translateX(52px); transform: translateX(52px)}"
           ".button {"
           "background-color: #4CAF50; /* Green */"
           "border: none;"
           "color: white;"
           "padding: 32px 32px;"
           "text-align: center;"
           "text-decoration: none;"
           "display: inline-block;"
           "font-size: 16px;"
           "width: 10.0rem;"
           "height: 10.0rem;"
           "border-radius: 50%;"
           "}"
           ".buttonOn {background-color: #f44336;}"
           ".buttonOff {background-color: #555555;}"
           "</style>"
           "</head><body>"
           "<h1>ESP-01/01a Relay V4.0</h1>"
         );
  if (relayStatus == 0) {
    html += F("<div><form action='/turnOn' id='controlRelay'>" // input type='button'>On/Off</input></div>");
              "</form>"
              "<button type='submit' class='button buttonOn' form='controlRelay' value=Submit'>Turn On</button>"
              "</div>"
             );
  } else {
    html += F("<div><form action='/turnOff' id='controlRelay'>" // input type='button'>On/Off</input></div>");
              "</form>"
              "<button  class='button buttonOff' type='submit' form='controlRelay' value=Submit'>Turn Off</button>"
              "</div>"
             );

  }
  html += F("</body></html>\r\n");
  server.send(200, "text/html", html);
}

void loop() {
  server.handleClient();
}
