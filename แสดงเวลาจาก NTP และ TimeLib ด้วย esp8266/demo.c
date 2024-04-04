#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include <NTPClient.h>
#include <TimeLib.h>

const char *ssid     = "ชื่อap";
const char *password = "รหัสของap";

WiFiUDP ntpUDP;


NTPClient timeClient(ntpUDP, "time.nist.gov", 7 * 3600, 60000);
unsigned long unix_epoch;
char dateMsg[64];
char timeMsg[64];

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);
  while ( WiFi.status() != WL_CONNECTED ) {
    delay(500);
    Serial.print(".");
  }
  timeClient.begin();
}

void showRTC() {
  char dow_matrix[7][10] = {"SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"};
  byte x_pos[7] = {29, 29, 23, 11, 17, 29, 17};
  static byte previous_dow = 0;

  if ( previous_dow != weekday(unix_epoch) )   {
    previous_dow = weekday(unix_epoch);
  }

  sprintf( dateMsg, "%02u-%02u-%04u", day(unix_epoch), month(unix_epoch), year(unix_epoch) );
  sprintf( timeMsg, "%02u:%02u:%02u", hour(unix_epoch), minute(unix_epoch), second(unix_epoch) );
  Serial.println(dateMsg);
  Serial.println(timeMsg);

}

void loop() {
  timeClient.update();
  unix_epoch = timeClient.getEpochTime();   // get UNIX Epoch time

  showRTC();
  delay(500);
}
