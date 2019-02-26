#include <Wire.h>

byte slave_address = 7;
byte cmd;
int i = 0;
float d;
float s;
float r;


//Ort:PWM (blau),Direction (gelb),FG (grün)
//VR: 5,2,3    ✓ (rot)
//VL: 6,11,4   ✓ (blau)
//HR: 9,12,7   ✓ (grün)
//HL: 10,13,8  ✓ (schwarz)

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(5, OUTPUT);  //PWM PIN 5  with PWM wire 
  pinMode(6, OUTPUT);  //PWM PIN 6  with PWM wire
  pinMode(9, OUTPUT);  //PWM PIN 9  with PWM wire
  pinMode(10, OUTPUT); //PWM PIN 10  with PWM wire
  pinMode(2, OUTPUT);  //direction control PIN 2 with direction wire
  pinMode(11, OUTPUT); //direction control PIN 11 with direction wire
  pinMode(12, OUTPUT); //direction control PIN 12 with direction wire
  pinMode(13, OUTPUT); //direction control PIN 13 with direction wire
  Wire.begin(slave_address);  //I2C wird initialisiert
  analogWrite(5, 255);
  analogWrite(9, 255);
  analogWrite(6, 255);
  analogWrite(10, 255);
}

void loop() {
  
  Wire.onReceive(ReadI2C);
  //ReadI2C();
  //delay(50);
}  
  

void moveF() {
  Serial.println("***moveF***");
  analogWrite(5, s-11-4);
  analogWrite(9, s-4);
  analogWrite(6 , s-11);
  analogWrite(10, s);
  digitalWrite(2, HIGH);
  digitalWrite(12, HIGH);
  digitalWrite(11, LOW);
  digitalWrite(13, LOW);
}

void moveB() {
  Serial.println("***moveB***");
  analogWrite(5, s);
  analogWrite(9, s);
  analogWrite(6, s);
  analogWrite(10, s);
  digitalWrite(2, LOW);  
  digitalWrite(12, LOW);
  digitalWrite(11, HIGH);
  digitalWrite(13, HIGH);
}

void stopM() {
  Serial.println("---stopM---");
  analogWrite(5, 255);
  analogWrite(9, 255);
  analogWrite(6, 255);
  analogWrite(10, 255);
  digitalWrite(2, LOW);  
  digitalWrite(12, LOW);
  digitalWrite(11, HIGH);
  digitalWrite(13, HIGH);
}


void moveR() {
  FoBoLoR();
  delay(100);
    for(int j = 0;j<8;j++)  {
    i += pulseIn(7, HIGH, 500000); //SIGNAL OUTPUT PIN 9 with  white line,cycle = 2*i,1s = 1000000us，Signal cycle pulse number：27*2
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
  Serial.print("t real = ");
  Serial.println(t - 175);
  delay(t - 100);
  analogWrite(5, 255);
  analogWrite(9, 255);
  analogWrite(6, 255);
  analogWrite(10, 255);
  i = 0;
}

void FoBoLoR() {
  if (d == 1) {
    moveF();
  }
  else if (d == 2) {
    moveB();
  }
  else if (d == 3) {
    turnL();
  }
  else if (d == 4) {
    turnR();
  }
}

void turnL() {
  analogWrite(5, s-11-4-15);
  analogWrite(9, s-4-15);
  analogWrite(6 , s-11-25);
  analogWrite(10, s-25);
  digitalWrite(2, HIGH);
  digitalWrite(12, HIGH);
  digitalWrite(11, HIGH);
  digitalWrite(13, HIGH);
}

void turnR() {
  
}

void ReadI2C() {
  Serial.println("-----Start I2C-----");
  int AnzahlBytes = Wire.available();
  if (AnzahlBytes == 2) {
    cmd = Wire.read();     //cmd
    int _ = Wire.read();
    stopM();
  }
  else if (AnzahlBytes == 3) {
    cmd = Wire.read();     //cmd
    d = Wire.read();            //Liste wird ausgelesen
    s = Wire.read();
    FoBoLoR();
  }
  else if (AnzahlBytes == 4) {
    cmd = Wire.read();     //cmd
    d = Wire.read();            
    s = Wire.read();
    r = Wire.read();
    moveR();
  }
}







  
