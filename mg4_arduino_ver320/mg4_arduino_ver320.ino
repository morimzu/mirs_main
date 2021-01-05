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
  Serial.begin(57600);
}

void loop() {
  //test_batt();
  int i = 0;  // orderの配列番号
  int k = 2;  // 数字の桁数
  double act1 = 0.0;
  double act2 = 0.0;
  int t = 0;  //制御対象の判断に用いる変数
  int sign = 1;   // 制御値の正負を決める
  
  enum MOTOR {
    M1, M2, L1, L2
  };
  
  int session = 0;  //命令文の中のどの要素なのかを示す
  // 0: 制御対象 1: 制御内容_L 2: 制御内容_R 3:
  
  while(true){
    if(Serial.available() > 0){
      val = Serial.read();
      //Serial.println(val);
    }
    //Serial.println(val);

    if(val == ';') {
      Serial.println("session");
      Serial.println(session);
      session++;
      k=2;
      continue;
      /*
      // sessionごとにpwmの桁数を決定している
      switch(session){
        case 0:
          k = 2;
        case 1:
          k = 3;
          break;
        case 2:
          k = 3;
          break;
        default:
          //Serial.println("NG: session error");
          Serial.println(session);
          Serial.println("NG");
      }
      continue;
      */
    }
    
    if(val == ':') { //命令の終わりの認識
      Serial.println("t");
      
      Serial.println(t);
      if(t == 20) {
        //走行制御の命令文がきたら
        /*
        Serial.print("act1: ");
        Serial.println(act1);
        Serial.print("act2: ");
        Serial.println(act2);
        Serial.print("times: ");
        Serial.println(times);
        */
        Serial.println(act1);
        Serial.println(act2);
        Serial.println("RUN");
        test_run_ctrl(STR, act1, act2);
        
      } else if(t == 40) {
        //LED制御の命令文がきたら
        led_set(act1);
        
      } else if(t == 50) {
        //回転の命令が来たら
        test_run_ctrl(ROT, act1, act2);
      }
      
      Serial.println("OK");
      
      // 一時的に使用していた変数の初期化
      val = 0;
      session = 0;
      k = 2;
      t = 0;
      act1 = 0;
      act2 = 0;
      sign = 1;
      session = 0;
      break;  //次の命令を読むためのループにうつる
    }
    
    order[i] = val;
    
    switch(session) {
      case 0: // 制御対象
        //Serial.println(session);
        Serial.println(encoder(val));
        t += encoder(val);
        break;
        
      case 1:
        //Serial.println(session);
        //Serial.println(encoder(val));
        if(encoder(val) == -1) {
          sign = -1;
        } else if(val=='.') {
          delay(0);
        } else {
          //Serial.println(encoder(val));
          //Serial.println(sign * pow(10, (float)k - 1.0));
          act1 += sign * encoder(val) * pow(10, (float)k - 1.0);
          k = k-1;
        }
        //Serial.println(act1);
        //Serial.println("act1");
        break;
        
      case 2:
        //Serial.println(session);
        if(encoder(val) == -1) {
          sign = -1;
        } else if(val=='.') {
          delay(0);
        } else {
          //Serial.println(encoder(val));
          //Serial.println(sign * pow(10, (float)k - 1.0));
          act2 += sign * encoder(val) * pow(10, (float)k - 1.0);
          k = k-1;
        }
        //Serial.println(act2);
        //Serial.println("act2");
        break;
        
      default:
        Serial.println("NG: selected session is unknown.");
        Serial.println(session);
        break;
    }
    
    k--;
    i++;
  }
  
}

int encoder(char number) { //複数桁の数値をint型に直す
  switch (number) {
    case '-': return -1;break;
    case '0': return 0;break;
    case '1': return 1;break;
    case '2': return 2;break;
    case '3': return 3;break;
    case '4': return 4;break;
    case '5': return 5;break;
    case '6': return 6;break;
    case '7': return 7;break;
    case '8': return 8;break;
    case '9': return 9;break;
    case 'r': return 20;break;
    case 'M': return 30;break;
    case 'L': return 40;break;
    case 't': return 50;break;
    default: return 0;break;
  }
}
