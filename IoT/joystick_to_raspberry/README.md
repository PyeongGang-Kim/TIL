# 아두이노 보드 블루투스 통신

아두이노 보드에서 소프트웨어시리얼 헤더를 사용하면 블루투스 통신이 가능하다.

```c++
#include <SoftwareSerial.h>
SoftwareSerial BTSerial(12, 13); //(TX, RX)의 핀 번호
```

위와 같이 선언을 하면 아두이노 보드의 12, 13번 핀을 TX, RX로 사용한 블루투스 통신을 하겠다는 의미이다.

 

셋업을 하기 전에 기본적으로 사용할 변수들을 선언해 준다.

```c++
const int joystick_x = A0;    
const int joystick_y = A1;
const int joystick_A = 2;
const int joystick_B = 3;
const int joystick_C = 4;
const int joystick_D = 5;
const int joystick_E = 6;
const int joystick_F = 7;
int sum;
int A, B, Au, Bu, u;
int button_chk;
int tmp;
int cnt;
```

조이스틱 버튼과 조이스틱 레버에 각 각 해당하는 핀을 넣어 알아보기 쉽게 만들어 줬다.



```c++
void setup()  
{
  pinMode ( joystick_A, INPUT_PULLUP );
  pinMode ( joystick_B, INPUT_PULLUP );
  pinMode ( joystick_C, INPUT_PULLUP );
  pinMode ( joystick_D, INPUT_PULLUP );
  pinMode ( joystick_E, INPUT_PULLUP );
  pinMode ( joystick_F, INPUT_PULLUP );
  Serial.begin(9600);
  Serial.println("Hello!");
  BTSerial.begin(9600);  // set the data rate for the BT port
  button_chk = 0;
  cnt = 0;
}
```

초기화 작업이 진행되는 부분이다. 내가 원하는 조이스틱 버튼에 해당하는 핀에 입력받는 타입이라고 지정해주었다.

Serial.begin(9600)은 보드레이트 9600으로 동작할 것이라고 선언하는 부분이다.

BTSerial.begin(9600)은 블루투스 통신을 9600 바우드로 지정하겠다는 의미이다.



```c++
void loop()
{
  // BT –> Data –> Serial
//  if (BTSerial.available()) {
//    /*
//    
//    Serial.write(BTSerial.read());
//    */
//  }
//  // Serial –> Data –> BT
  sum = 0;
  sum = !digitalRead(joystick_A) << 1;
  sum = (sum + !digitalRead(joystick_B)) << 1;
  sum = (sum + !digitalRead(joystick_C)) << 1;
  sum = (sum + !digitalRead(joystick_D)) << 1;
  sum = (sum + !digitalRead(joystick_E)) << 1;
  sum = (sum + !digitalRead(joystick_F));
  if (sum == tmp) {
    button_chk = 0;
  }
  else {
    tmp = sum;
    if (tmp) {
      button_chk = 1;
    }
    else {
      button_chk = 0;
    }
  }
  A = map(analogRead(joystick_x), 0, 1023, -127, 127);
  B = map(analogRead(joystick_y), 0, 1023, -127, 127);
  u = (A*A+B*B) >> 5;
  if (button_chk || u) {
    Au = ((A+8) >> 4);
    Bu = ((B+8) >> 4);
    BTSerial.write(sum);
    BTSerial.write(Au + 127);
    BTSerial.write(Bu + 127);
    delay(1);
    Serial.println(Au);
    Serial.println(Bu);
    Serial.println(sum);
    Serial.println( 400 - (u >> 2));
//    delay ( 400 - (u >> 2));
    delay(10);
    cnt += 1;
    if (cnt >= 15) {
      cnt = 0;
      delay(130);
    }
  
  }
}
```

각 조이스틱 버튼은 1 / 0 으로 나뉘게 되므로 하나의 조이스틱 버튼에 1개의 비트만 있으면 된다. 그래서 이 센서 데이터들을 sum이라는 변수에 해당 값을 더하고 쉬프트 하는 방식으로 sum 변수의 각 자리에 해당시켰다.

map(analogRead(joystick_x), 0, 1023, -127, 127) 이 부분은

조이스틱 x로부터 읽어온 아날로그 데이터는 0~1023인데 -127~127 사이의 값으로 변환시켜 받겠다는 의미이다.

이렇게 하게 되면 양의 값만 들어오는 센서 데이터가 방향에 따라 음, 양으로 변하게 된다.

이후 방향의 크기를 계산하기 위한 부분이 u라는 변수이다.

```c++
u = (A*A+B*B) >> 5;
```

x축제곱 + y축 제곱은 r제곱에 비례함을 이용하여 u의 크기가 일정 이상 될 때 혹은 버튼값이 있을 때에만 센서 데이터를 전송하기 위하여 아래의 조건문을 사용한다.

```c++
if (button_chk || u)
```



BTSerial.write() 함수는 1 바이트단위로 블루투스 통신을 통해 이진 데이터가 전송된다. 따라서 이를 적절하게 변환하여 0~255 사이에 들어가는 값으로 변환을 해 준다.



BTSerial.write()의 경우 너무 빠르게 데이터를 전송하려고 하면 각 바이트 단위로 전송하는 것이 아니라, 데이터를 모아뒀다가 한번에 전송하는 문제점이 존재한다. 따라서 데이터를 한번 전송할 때마다 일정 딜레이를 줘서 해결하였다.



이로써 아두이노 보드에서 블루투스를 통하여 조이스틱 정보를 전송할 준비를 마쳤다.