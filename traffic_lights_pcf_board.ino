#include <Adafruit_PCF8574.h>

Adafruit_PCF8574 pcf;

int incomingByte; // variable to read incoming serial data

void setup() {
  Serial.begin(9600);
  if (!pcf.begin(B0111000, &Wire)) {
    Serial.println("Couldn't find PCF8574");
    while (1);
  }
  for (int p=1; p<7; p++){
    pcf.pinMode(p, OUTPUT);
  }
  for(int p=7; p<9; p++){
    pcf.pinMode(p, INPUT);
  }
}

void loop() {
  // check to see if there is incoming serial data:
  if (Serial.available() > 0) {
//    Serial.print(Serial.available());
    // read the oldest byte in serial buffer:
    incomingByte = Serial.read();
   
    if (incomingByte == 'A') {
      pcf.digitalWrite(1, LOW);
      pcf.digitalWrite(2, HIGH);
      pcf.digitalWrite(3, HIGH);
    }
    
    if (incomingByte == 'B') {
      pcf.digitalWrite(1, HIGH);
      pcf.digitalWrite(2, LOW);
      pcf.digitalWrite(3, HIGH);

    }

    if (incomingByte == 'C') {
      pcf.digitalWrite(1, HIGH);
      pcf.digitalWrite(2, HIGH);
      pcf.digitalWrite(3, LOW);

    }
    if (incomingByte == 'D') {
      pcf.digitalWrite(4, LOW);
      pcf.digitalWrite(5, HIGH);
      pcf.digitalWrite(6, HIGH);

    }
    if (incomingByte == 'E') {
      pcf.digitalWrite(4, HIGH);
      pcf.digitalWrite(5, LOW);
      pcf.digitalWrite(6, HIGH);

     }
    if (incomingByte == 'F') {
      pcf.digitalWrite(4, HIGH);
      pcf.digitalWrite(5, HIGH);
      pcf.digitalWrite(6, LOW);
      
     }
    Serial.println(incomingByte);
  }
//  else {
//   
//  }
}
