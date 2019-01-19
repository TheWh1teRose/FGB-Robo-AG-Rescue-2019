#include <Wire.h>

byte slave_address = 7;
byte cmd;
int i = 0;
float d;
float s;
float r;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(10, OUTPUT); //PWM PIN 10  with PWM wire
  pinMode(11, OUTPUT);//direction control PIN 11 with direction wire
  Wire.begin(slave_address);  //I2C wird initialisiert
}

void loop() {
  ReadI2C();
}  
  

void moveF() {
  Serial.println("***moveF***");
  analogWrite(11, s);
  digitalWrite(10, HIGH);
}

void moveB() {
  Serial.println("***moveB***");
  analogWrite(11, s);
  digitalWrite(10, LOW);
}

void stopM() {
  Serial.println("---stopM---");
  analogWrite(11, 255);
}

void moveR() {
  FoB();
  delay(100);
  for(int j = 0;j<8;j++)  {
    i += pulseIn(9, HIGH, 500000); //SIGNAL OUTPUT PIN 9 with  white line,cycle = 2*i,1s = 1000000us，Signal cycle pulse number：27*2
  }
  i = i >> 3;
  Serial.print(111111 / i); //speed   r/min  (60*1000000/(45*6*2*i))
  Serial.println("  r/min");
  float rpm = (111111 / i); //Die Formel fuer Drehungen pro Sekunde
  float rps = rpm / 60;
  float t = (r / rps)*1000;     //Die Zeit in ms die benoetigt wird um mit gegebenen Speed die angegebenen Umdrehungen zu schaffen
  Serial.print("i = ");
  Serial.println(i);
  Serial.print(rpm); //speed   r/min  (60*1000000/(45*6*2*i))
  Serial.println("  r/min"); 
  Serial.print(rps);
  Serial.println(" r/s");
  Serial.print("t = ");
  Serial.println(t);
  delay(t - 175);
  analogWrite(11, 255);
  i = 0;
}

void FoB() {
  if (d == 1) {
    moveF();
  }
  else {
    moveB();
  }
}

void LoR() {
  if (d == 1) {
    turnL();
  }
  else {
    turnR();
  }
}

void turnL() {
  
}

void turnR() {
  
}

void ReadI2C() {
  int AnzahlBytes = Wire.available();
  if (AnzahlBytes == 1) {
    stopM();
  }
  else if (AnzahlBytes == 2) {
    LoR();
  }
  else if (AnzahlBytes == 3) {
    cmd = Wire.read();     //cmd
    d = Wire.read();            //Liste wird ausgelesen
    s = Wire.read();
    FoB();
  }
  else if (AnzahlBytes == 4) {
    cmd = Wire.read();     //cmd
    d = Wire.read();            
    s = Wire.read();
    r = Wire.read();
    moveR();
  }
}







  
