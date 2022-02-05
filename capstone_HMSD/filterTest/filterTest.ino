#include <SimpleKalmanFilter.h>
#define Flex A0
#define Pressure A1
float Pread, Fread, Pkal, Fkal;
SimpleKalmanFilter simpleKalmanFilter(20,10,0.01);
const long SERIAL_REFRESH_TIME = 100;
long refresh_time=0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  readsensor();
  filter();
  if (millis() > refresh_time) {
    Serial.print(Pread,4);
    Serial.print(",");
    Serial.print(Pkal,4);
    Serial.println();
    
    refresh_time = millis() + SERIAL_REFRESH_TIME;
  }

}

  void readsensor()
{
  Pread= analogRead(Pressure)*100/1024;
  //if(Pread<0) Pread=31;
  Fread= analogRead(Flex)*100/1024;
}

void filter()
{
  Pkal=simpleKalmanFilter.updateEstimate(Pread);
  Fkal=simpleKalmanFilter.updateEstimate(Fread);
}
