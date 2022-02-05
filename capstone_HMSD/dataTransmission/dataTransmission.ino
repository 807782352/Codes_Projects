#include <EEPROM.h>
int x=0;
const int ledPin = 13; // pin the LED is attached to
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);
  x=EEPROM.read(0);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (Serial.available()){
    x = Serial.readString().toInt();
//    Serial.print(x);
    EEPROM.update(0,x);
//    Serial.println();
  }
//  else{
////    x=EEPROM.read(0);
////    Serial.println(x);
////    Serial.print("Serial unabailable");
////    Serial.println();
// }
//  //Serial.println();

  if (x == 133) {
    digitalWrite(ledPin, HIGH);
//    Serial.println("Getting H"); //print out to serial monitor to check state
      }
  else if (x != 133){
    digitalWrite(ledPin, LOW);
//    Serial.println("Getting L"); //print out to serial monitor to check state
  }
  //Serial.println(x);
  delay(20);
}
