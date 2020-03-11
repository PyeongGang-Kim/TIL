# 부하테스트

## 준비사항

JMeter 5.2.1



## 측정 시나리오

REST API 서버의 성능 측정

가장 많이 사용될 URL은 메인 페이지에 사용될 목록을 가져오는  getallsurvey 메서드이다.

|                URL                | 요청 방식 |
| :-------------------------------: | :-------: |
| http://13.124.194.207/api/surveys |    GET    |



이 주소를 다음과 같은 설정으로 테스트 해 본다.

### 테스트 설정

startup time 20, shutdown time 10, hold load 60

start hreads count 100

![setting 100](C:/Users/user/self-online/day3/image/setting 100.png)



### 결과

response time

![rt 100-1](C:/Users/user/self-online/day3/image/rt 100-1.png)



TSP

![tps 100-1](C:/Users/user/self-online/day3/image/tps 100-1.png)

startup time 20, shutdown time 10, hold load 60

start hreads count 100

으로 측정해본 결과 01:06이 되는 순간부터 failure가 급격하게 발생하는 것을 확인할 수 있었습니다.

서버가 90초를 버티지 못한 경우입니다.



### 가능한 사용자 수

현재 사용 가능한 사용자 수를 확인하기 위하여 다른 설정은 유지한 채 start threads count만 변경하면서 response time, TPS를 확인해 보았습니다.



### start threads count - 50

resopnse time

![rt 50-1](C:/Users/user/self-online/day3/image/rt 50-1.png)

TPS

![tps 50-1](C:/Users/user/self-online/day3/image/tps 50-1.png)



### start threads count - 15

resopnse time

![rt 15-1](C:/Users/user/self-online/day3/image/rt 15-1.png)

TPS

![tps 15-1](C:/Users/user/self-online/day3/image/tps 15-1.png)



### start threads count - 10

resopnse time

![rt 10-1](C:/Users/user/self-online/day3/image/rt 10-1.png)

TPS

![tps 10-1](C:/Users/user/self-online/day3/image/tps 10-1.png)



### 분석

threads count를 50, 15, 10으로 줄여가면서 확인해 본 결과 90초동안 큰 문제가 발생하지 않는 thread count는 10 이었습니다.

메인페이지에 대해서 최대 열명의 사용자가 문제 없이 사용할 수 있을 것으로 추정됩니다.



## 개선방안

메인 페이지에서 목록 데이터를 전부 다 받아오는 것이 서버에 큰 부담이 되는 중입니다.

현재 웹 페이지는 모든 데이터를 한번에 가져오고 그걸 그냥 가지고 있다가 필요시(스크롤이 다 된 경우) 보여줄 아이템 리스트에 추가하는 방식으로 무한 스크롤을 구현하였습니다.

이러한 방식의 경우 추후에 목록 데이터가 커지면 커질수록 문제가 발생할 것으로 추정됩니다.

또한 사용되지 않고 의미 없는 데이터가 많기 때문에 한번에 모든 데이터를 가져오는 것이 아닌, 당장 보여줄 데이터만 요청해서 받아오고 나머지 데이터는 필요 시 서버에 요청해서 필요한 데이터만 받아오는 방식으로 변경해야 할 것입니다.