# TIL(Today I Learned)
https://docs.python.org/ko/3/tutorial/stdlib.html#operating-system-interface

https://www.edx.org/

https://docs.google.com/spreadsheets/d/1f5Il6slzWfrAKskzKvx23YjrtxpqtlsBBm_AmZtD4YQ/edit#gid=0


https://mygumi.slack.com/messages/CL0E0QZ5F/

vs코드의 확장프로그램 excel viewer 설치



마크다운 이미지 넣고싶을 때 ![]() 경로는 상대경로로, 역슬래시가 기본이지만 정슬래시로 바꾼후 입력해준다.







파이썬 스택 구현 고려사항

리스트 사용해서 스택을 구현하는 경우(append, pop(-1)이용)



구현이 용이한 것이 장점

단점은 리스트 크기를 변경하는 작업은 내부적으로 큰 overhead 발생 작업으로 많은 시간이 소요됨



해결방법

1.리스트의 크기가 변동되지 않도록 배열처럼 크기를 미리 정해놓고 사용하는 방법

2.동적 연결리스트를 이용하여 저장소를 동적으로 할당하여 스택을 구현하는 방법

(구체적으로 어떻게??)



5칸배열

2칸짜리 4가지 방법

2칸짜리 2개인 3가지 방법



10칸배열

2칸짜리 9가지 방법

2칸짜리 2개인 7 6 5 4 3 2 1



변수 for문 중에서 원하는 위치 (i=13이 될 때)에서 디버깅하는 방법은?