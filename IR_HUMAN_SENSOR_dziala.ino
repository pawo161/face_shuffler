    /////////////////////////////////////////////////////////////////
   //             Arduino PIR sensor Tutorial           v1.00     //
  //       Get the latest version of the code here:              //
 //      http://educ8s.tv/arduino-pir-sensor-tutorial           //
/////////////////////////////////////////////////////////////////

#include <Keyboard.h>
int ledPin = 6;
int pirPin = 9;
unsigned long val = 0;

void setup() 
{
  pinMode (ledPin,OUTPUT);
  pinMode (pirPin, INPUT);
  Keyboard.begin();
}
void loop () 
{
  val = digitalRead(pirPin);
  digitalWrite(ledPin,val);

if (val == 1){
  digitalWrite(ledPin,LOW);
  Serial.println("motion detected");
  USBDevice.wakeupHost();
  Keyboard.write('m');
  delay(3000);
}
else
  Serial.println("scanning");

}
