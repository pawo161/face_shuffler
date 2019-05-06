///////////////////////code created by///////////////////////
//////////////////////KJ's electronics//////////////////////
int ledState = LOW;             // ledState used to set the LED

// Generally, you should use "unsigned long" for variables that hold time
// The value will quickly become too large for an int to store
unsigned long previousMillis = 0;        // will store last time LED was updated

// constants won't change :
const long interval = 200;         

int PIR_output=5; // output of pir sensor
int led=3; // led pin
int green=2;// buzzer pin
int pwr=4;
void setup() {
pinMode(PIR_output, INPUT);// setting pir output as arduino input
pinMode(led, OUTPUT);//setting led as output
pinMode(green, OUTPUT);//setting buzzer as output
pinMode(pwr,OUTPUT);
digitalWrite(pwr,HIGH);
Serial.begin(9600);//serial communication between arduino and pc
}
void loop() {
if(digitalRead(5) == HIGH) // reading the data from the pir sensor
{
 unsigned long currentMillis = millis();
 
  if(currentMillis - previousMillis >= interval) {
    // save the last time you blinked the LED 
    previousMillis = currentMillis;   

    // if the LED is off turn it on and vice-versa:
    if (ledState == LOW)
      ledState = HIGH;
    else
      ledState = LOW;

    // set the LED with the ledState of the variable:
    digitalWrite(led, ledState);
  }
 digitalWrite(green, LOW); // setting buzzer to high
 Serial.println("motion detected");
 
}
else {
 digitalWrite(led, LOW); // setting led to low
 digitalWrite(green, HIGH); // setting buzzer to low
 Serial.println("scanning");
}
}
