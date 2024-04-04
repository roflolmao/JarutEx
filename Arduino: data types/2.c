void setup() {
  Serial.begin(115200);
  // Input (data)
  byte temp[] = {35,34,35,38,39};
  float avgTemp, sumTemp;
  // Process (algorithm)
  sumTemp = temp[0]+temp[1]+temp[2]+temp[3]+temp[4];
  avgTemp = sumTemp / 5.0;
  // Output
  Serial.print("Temperature:");
  Serial.print(temp[0]);
  Serial.print(",");
  Serial.print(temp[1]);
  Serial.print(",");
  Serial.print(temp[2]);
  Serial.print(",");
  Serial.print(temp[3]);
  Serial.print(",");
  Serial.println(temp[4]);
  Serial.print("Sum of temperature:");
  Serial.println(sumTemp);
  Serial.print("Average of temperature:");
  Serial.println(avgTemp);
}

void loop() {
}
