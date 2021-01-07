//ライブラリインクルード
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define LED_COUNT 60
#define DIGITAL_PIN 10
#define BRIGHTNESS 150

Adafruit_NeoPixel strip( LED_COUNT, LED_PIN , NEO_GRB + NEO_KHZ800);

void led_open() {
  //初期化処理
  #if defined(__AVR_Atiny85__) && (F_CPU == 16000000)
    clock_prescale_set(clock_dev_1);
  #endif
  
  strip.begin();
  strip.show();
  strip.setBrightness(BRIGHTNESS);
}
/*
デフォルトの文
void loop() {

  ///色を設定
  //第一引数：何個目のLEDを光らせるか
  //第二引数：色を設定(RGB)
  led.setPixelColor( 1, led.Color(255,255,255));

  ///設定した情報をテープに送る！
  led.show();

}
*/

void led_set(int times) {
  colorWipe(strip.Color(0, 0, 255), 50);     //LEDを青色で点灯
  colorWipe(strip.Color(0, 0, 0, 255), 50);  //消灯
}


void colorWipe(uint32_t color, int wait){
  for(int i=0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, color);
    strip.show();
    delay(wait);    
  }
}
