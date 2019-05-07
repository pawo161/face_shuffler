int ledPin = 6;
int pirPin = 9;
unsigned long val = 0;

void setup() 
{
  Serial.begin(9600);
  pinMode (ledPin,OUTPUT);
  pinMode (pirPin, INPUT);
}
void loop () 
{
  val = digitalRead(pirPin);
  digitalWrite(ledPin,val);

if (val == 1){
  digitalWrite(ledPin,LOW);
  Serial.println("motion_detected");
  Serial.write(45);
  delay(3000);
}
else
  digitalWrite(ledPin,HIGH);
}
