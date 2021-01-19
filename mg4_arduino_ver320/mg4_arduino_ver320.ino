/*
  Ver1.0からの変更点　　　RaspberryPi と２バイトデータのシリアル通信をできるようにした
  Ver2.0からの変更点　　　RaspberryPi とのシリアル通信の速度を9600bps から 115200bpsに変更した
*/
byte val = 0;
char order[30];

#include "define.h"
#include<string.h>

int btoi(char number);

void setup() {
  io_open();
  encoder_open();
  motor_open();
  raspi_open();
  led_open();
  Serial.begin(115200);
}
  double act1 = 0.0;
  double act2 = 0.0;
  
void loop() {
  //test_batt();
  if(Serial.available() > 0) {
    serial_com();
    Serial.println("OK");
  }
}
