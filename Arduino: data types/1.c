void setup() {
  Serial.begin(115200);
  // Input (data)
  byte temp0, temp1, temp2, temp3, temp4;
  float avgTemp, sumTemp;
  temp0 = 35;
  temp1 = 34;
  temp2 = 35;
  temp3 = 38;
  temp4 = 39;
  // Process (algorithm)
  sumTemp = temp0+temp1+temp2+temp3+temp4;
  avgTemp = sumTemp / 5.0;
  // Output
  Serial.print("Temperature:");
  Serial.print(temp0);
  Serial.print(",");
  Serial.print(temp1);
  Serial.print(",");
  Serial.print(temp2);
  Serial.print(",");
  Serial.print(temp3);
  Serial.print(",");
  Serial.println(temp4);
  Serial.print("Sum of temperature:");
  Serial.println(sumTemp);
  Serial.print("Average of temperature:");
  Serial.println(avgTemp);
}

void loop() {
}
