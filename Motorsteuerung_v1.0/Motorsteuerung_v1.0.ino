#include <Wire.h>


byte slave_address = 7;
float t = 0;
int nowmillis;
long i;
int d;
int s;
int r;

void setup() {
  // put your setup code here, to run once:
  pinMode(10, OUTPUT);        //PWM PIN 10  with PWM wire
  pinMode(11, OUTPUT);        //direction control PIN 11 with direction wire
  Wire.begin(slave_address);  //I2C wird initialisiert
}

int * ReadI2C() {
  int AnzahlBytes = Wire.available();
  Serial.print(AnzahlBytes);
  byte b = Wire.read();       //cmd
  byte bd = Wire.read();      //bytes werden ausgelesen
  byte bs = Wire.read();
  byte br = Wire.read();
  d = (int) bd;           //bytes werden in int umgewandelt und in Array gespeichert
  s = (int) bs;
  r = (int) br;
}

void directions(int d, int s) {
  if (d == 1) {               //geradeaus fahren
    analogWrite(11, s);
    digitalWrite(10, HIGH);
    analogWrite(2, s);
    digitalWrite(3, HIGH);
  }
  if (d == 2) {                 //rückwärts fahren
    analogWrite(11, s);
    digitalWrite(10, LOW);
    analogWrite(2, s);
    digitalWrite(3, LOW);
  }
  if (d == 3) {                 //links drehen
    analogWrite(11, s);
    digitalWrite(10, LOW);
    analogWrite(2, s);
    digitalWrite(3, HIGH);
  }
  if (d == 4) {                 //rechts drehen
    analogWrite(11, s);
    digitalWrite(10, HIGH);
    analogWrite(2, s);
    digitalWrite(3, LOW);
  }
}

void moveM() {
  nowmillis = millis();
  while (t <= millis() - nowmillis) {
    directions(d, s);
    for (int j = 0; j < 8; j++)  {
      i += pulseIn(9, HIGH, 500000);
    }
    i = 0 >> 3;
    int rps = (111111 / i) / 60; //Die Formel für Drehungen pro Sekunde
    t = (r / rps) * 1000;     //Die Zeit die benötigt wird um mit gegebenen Speed die angegebenen Umdrehungen zu schaffen
  }
  analogWrite(11, 255);       //Motoren werden gestoppt
  analogWrite(2, 255);
}

void loop() {
  Wire.onReceive(moveM);      //Sobald er etwas entfängt wird diese Funktion ausgeführt
  //Beendigungsbestätigung?
}





