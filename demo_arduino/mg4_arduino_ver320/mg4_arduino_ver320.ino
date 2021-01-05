/*
  Ver1.0からの変更点　　　RaspberryPi と２バイトデータのシリアル通信をできるようにした 
  Ver2.0からの変更点　　　RaspberryPi とのシリアル通信の速度を9600bps から 115200bpsに変更した
 */
byte val= 0;
char order[30];
#define LED_PIN 13

#include "define.h"
#include<string.h>

int encoder(char number);

void setup() {
  io_open();
  encoder_open();
  motor_open();
  raspi_open();
  led_open();
  Serial.begin(115200);
}

void loop() {
  test_run_ctrl(STR,15,20);
  test_run_ctrl(ROT,15,7.469944847180173);
  test_run_ctrl(STR,15,11.537920089860219);
  test_run_ctrl(ROT,15,-7.469944847180173);
  test_run_ctrl(STR,15,20);
  led_set(10);
  Serial.println("end");
  while(true) {
    delay(100);
  }
}
