/*
  Ver1.0からの変更点　　　RaspberryPi と２バイトデータのシリアル通信をできるようにした
  Ver2.0からの変更点　　　RaspberryPi とのシリアル通信の速度を9600bps から 115200bpsに変更した
*/
byte val = 0;
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
  if (Serial.available() > 0) {
    val = Serial.read();
  }
  if (val == 'a') {
    test_run_ctrl(STR, 15, 20);
    test_run_ctrl(ROT, 15, 10.077673241270588);
    test_run_ctrl(STR, 15, 85.72257578957833);
    test_run_ctrl(ROT, 15, -10.077673241270588);
    test_run_ctrl(STR, 15, 20);
    led_set(10);

    test_run_ctrl(STR, 15, 20);
    test_run_ctrl(ROT, 15, -10.077673241270588);
    test_run_ctrl(STR, 15, 85.72257578957833);
    test_run_ctrl(ROT, 15, 10.077673241270588);
    test_run_ctrl(STR, 15, 20);
    led_set(10);

    test_run_ctrl(STR, 15, 20);
    test_run_ctrl(ROT, 15, 10.077673241270588);
    test_run_ctrl(STR, 15, 85.72257578957833);
    test_run_ctrl(ROT, 15, -10.077673241270588);
    test_run_ctrl(STR, 15, 20);
    led_set(10);
  }
  Serial.println("end");
  while (true) {
    delay(100);
  }
}
