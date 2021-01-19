void serial_com() {
  int i = 0;  // orderの配列番号
  int k = 2;  // 数字の桁数
  int sign = 1;   // 制御値の正負を決める
  int t = 0; // 制御対象を示す変数

  int session = 0;  //命令文の中のどの要素なのかを示す
  // 0: 制御対象,  1: 制御内容1,  2: 制御内容2
  while (Serial.available() > 0) {
    val = Serial.read();

    if (val == 'a') continue; //aはデータなしを示す．断続的にデータが送信されてしまった場合に対応させている．

    if (val == ';') {
      Serial.println(session);
      session++;
      k = 2;
      continue;
    }

    else if (val == ':') { //命令の終わりの認識
      Serial.println("t");

      Serial.println(t);
      if (t == 20) {
        //走行制御の命令文がきたら
        Serial.println(act1);
        Serial.println(act2);
        Serial.println("RUN");
        test_run_ctrl(STR, act1, act2);

      } else if (t == 30) {
        //LED制御の命令文がきたら
        led_set();

      } else if (t == 40) {
        //回転の命令が来たら
        Serial.println(act1);
        Serial.println(act2);
        Serial.println("TURN");
        test_run_ctrl(ROT, act1, act2);
      }

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
    else {
      order[i] = val;

      switch (session) {
        case 0: // 制御対象
          Serial.println(session);
          Serial.println(serial_btoi(val));
          t += serial_btoi(val);
          break;

        case 1:
          if (serial_btoi(val) == -1) {
            sign = -1;
          } else if (val == '.') {
            delay(0);
          } else {
            act1 += sign * serial_btoi(val) * pow(10, (float)k - 1.0);
            k = k - 1;
          }
          break;

        case 2:
          if (serial_btoi(val) == -1) {
            sign = -1;
          } else if (val == '.') {
            delay(0);
          } else {
            act2 += sign * serial_btoi(val) * pow(10, (float)k - 1.0);
            k = k - 1;
          }
          break;

        default:
          Serial.println("NG: selected session is unknown.");
          Serial.println(session);
          break;
      }
    }

    i++;
    val = 'a';
  }
}

int serial_btoi(char number) { //複数桁の数値をint型に直す
  switch (number) {
    case '-': return -1; break;
    case '0': return 0; break;
    case '1': return 1; break;
    case '2': return 2; break;
    case '3': return 3; break;
    case '4': return 4; break;
    case '5': return 5; break;
    case '6': return 6; break;
    case '7': return 7; break;
    case '8': return 8; break;
    case '9': return 9; break;
    case 'r': return 20; break;
    case 'l': return 30; break;
    case 't': return 40; break;
  }
}
