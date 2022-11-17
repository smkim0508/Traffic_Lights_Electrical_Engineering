#include <Adafruit_PCF8574.h>

Adafruit_PCF8574 pcf;

int incomingByte; // variable to read incoming serial data
int p1=0;
int p2=0;
int p3=0;
int p4=0;
int p5=0;
int p6=0;

void setup() {
  Serial.begin(9600);
  if (!pcf.begin(B0111000, &Wire)) {
    Serial.println("Couldn't find PCF8574");
    while (1);
  }
  for (int p=0; p<6; p++){
    pcf.pinMode(p, OUTPUT);
  }
  for(int p=6; p<8; p++){
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
      p1 = 0;
      p2 = 0;
      p3 = 1;
    }
    
    if (incomingByte == 'B') {
      p1 = 0;
      p2 = 1;
      p3 = 0;
    }

    if (incomingByte == 'C') {
      p1 = 1;
      p2 = 0;
      p3 = 0;

    }
    if (incomingByte == 'D') {
      p4 = 0;
      p5 = 0;
      p6 = 1;

    }
    if (incomingByte == 'E') {
      p4 = 0;
      p5 = 1;
      p6 = 0;

     }
    if (incomingByte == 'F') {
      p4 = 1;
      p5 = 0;
      p6 = 0;
      
     }
    Serial.println(incomingByte);
  }
    if (p1 == 1){
      pcf.digitalWrite(0, LOW);
    }
    else {
      pcf.digitalWrite(0, HIGH);
    }
    
    if (p2 == 1){
      pcf.digitalWrite(1, LOW);
    }
    else {
      pcf.digitalWrite(1, HIGH);
    }

    if (p3 == 1){
      pcf.digitalWrite(2, LOW);
    }
    else {
      pcf.digitalWrite(2, HIGH);
    }

    if (p4 == 1){
      pcf.digitalWrite(3, LOW);
    }
    else {
      pcf.digitalWrite(3, HIGH);
    }

    if (p5 == 1){
      pcf.digitalWrite(4, LOW);
    }
    else {
      pcf.digitalWrite(4, HIGH);
    }

    if (p6 == 1){
      pcf.digitalWrite(5, LOW);
    }
    else {
      pcf.digitalWrite(5, HIGH);
    }
//    pcf.digitalWrite(4, HIGH);
//    pcf.digitalWrite(5, HIGH);
//    pcf.digitalWrite(6, LOW);
//  else {
//   
//  }
}
