int ledPin = 6;
int pirPin = 9;
int val = 0;

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
  Serial.println("motion_detected");
  digitalWrite(ledPin,LOW);
  delay(3000);
}
else
  digitalWrite(ledPin,HIGH);
}
