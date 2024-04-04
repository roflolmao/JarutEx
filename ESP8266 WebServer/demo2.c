#include <DHT.h>
#include <ESP8266WiFi.h>

#define AP_NAME "JarutEx"
#define AP_PASSWD "123456789"
IPAddress myIP(192, 168, 4, 1);
IPAddress gwIP(192, 168, 4, 10);
IPAddress subnet(255, 255, 255, 0);

DHT dht = DHT(5, DHT11); // D1
WiFiServer server(80);

float minC = 100.0f, maxC = 0.0f; // อุณหภูมิต่ำสุด/สูงสุด
float minH = 100.0f, maxH = 0.0f; // ความชื้นต่ำสุด/สูงสุด
float hic; // headt index ในหน่วย C
float hif;// headt index ในหน่วย F
float h; // ค่าความชื้น
float tc; // ค่าอุณหภูมิในหน่วย C
float tf; // ค่าอุณหภูมิในหน่วย F

void getDHT11() {
  h = dht.readHumidity();
  tc = dht.readTemperature();
  tf = dht.readTemperature(true);

  if (isnan(h) || isnan(tc) || isnan(tf)) {
    h = -1.0f;
    tc = -1.0f;
    tf = -1.0f;
    hic = -1.0f;
    hif = -1.0f;
    return;
  }

  hic = dht.computeHeatIndex(tc, h, false);
  hif = dht.computeHeatIndex(tf, h);

  if (minC > tc) {
    minC = tc;
  }
  if (maxC < tc) {
    maxC = tc;
  }
  if (minH > h) {
    minH = h;
  }
  if (maxH < h) {
    maxH = h;
  }
}

void setup() {
  Serial.begin(115200);
  Serial.println("\n\n\n");
  dht.begin();
  if (WiFi.softAPConfig( myIP, gwIP, subnet )) {
    if (WiFi.softAP(AP_NAME, AP_PASSWD, 8, false, 5)) {
      Serial.print("IP Address : ");
      Serial.println(WiFi.softAPIP());
    } else {
      Serial.println("softAP() failed!!");
      while (true);
    }
  } else {
    Serial.println("softAPConfig() failed!");
    while (true);
  }
  server.begin();
}

String htmlPage() {
  String html;
  getDHT11();
  html.reserve(2048);               // prevent ram fragmentation
  html = F("HTTP/1.1 200 OK\r\n"
           "Content-Type: text/html\r\n"
           "Connection: close\r\n"  // the connection will be closed after completion of the response
           "Refresh: 5\r\n"         // refresh the page automatically every 5 sec
           "\r\n"
           "<!DOCTYPE HTML>"
           "<html><head></head><body>"
           "<h1>DHT11</h1>");
  html += F("<div>Temperature:");
  html += tc;
  html += F("C/");
  html += tf;
  html += F("F</div>");
  html += F("<div>Huminity:");
  html += h;
  html += F("%</div>");
  html += F("<div>Temperature:");
  html += minC;
  html += F("C-");
  html += maxC;
  html += F("C</div>");
  html += F("<div>Huminity:");
  html += minH;
  html += F("%-");
  html += maxH;
  html += F("%</div>");
  html += F("</body></html>\r\n");
  return html;
}

void loop() {
  WiFiClient client = server.available();

  if (client)   {
    Serial.println("\n[Client connected]");
    while (client.connected()) {
      if (client.available()) {
        String req = client.readStringUntil('\r');
        Serial.print(req);
        if (req.indexOf("GET / HTTP/1.1")) {
          client.println(htmlPage());
          break;
        }
      }
    }

    while (client.available()) {
      client.read();
    }

    client.stop();
    Serial.println("[Client disconnected]");
  }
}
