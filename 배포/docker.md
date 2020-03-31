# docker

# 도커

## 도커란?

컨테이너 기반의 가상화 시스템

현재 os위에 서버 환경을 새롭게 구축(가상 환경으로)함으로써 내 현재 운영체제와 별개로 동작하는 서버를 구축한다.



## 도커의 장점

도커는 현재 운영체제에서 없는 파일들만 설치하기 때문에 쉽고 빠르게 서버 환경을 테스트 할 수 있고 용량 또한 적게 차지한다. 그리고 어떤 운영체제에서 구동하더라도 동일하게 작동하기 때문에(가상화) OS 이슈 발생이 적다.

또한 이러한 설정이 저장된 상태로 언제 서버를 구축하더라도 동일한 서버를 구축 가능하기 때문에 구축하는 시점마다 달라진 버전 때문에 발생하는 문제를 회피 할 수 있다.



## 도커 설치 방법

이 방법은 Hyper-V를 사용할 수 있는 윈도우 운영체제에서 적용 가능한 방법이다.

[도커 다운로드](https://hub.docker.com/editions/community/docker-ce-desktop-windows)



## 도커 실행 주의 사항

docker desktop 실행 시 관리자 권한으로 실행해야 무한 로딩 현상이 발생하지 않는다.



도커는 vmcompute를 사용하므로 이 서비스가 사용할 수 있어야 한다. 도커 실행 중 이 관련 에러가 발생한 경우

win+x > N 을 눌러 설정을 들어간다

업데이트 및 보안 화면에서 windows 보안을 클릭 후 앱 및 브라우저 컨트롤을 들어간다

Exploit Protection 설정을 누른다.

프로그램 설정 > 프로그램을 추가해 사용자 지정 > 정확한 파일경로 선택

파일 이름에 C:\Windows\System32\vmcompute.exe 입력 후 열기 클릭

프로그램 설정: vmcompute.exe 화면에서 흐름 제어 보호 (CFG) 항목의 시스템 설정 재정의 체크 해제 후 적용 클릭

win+x > A 눌러 명령 프롬포트(관리자) 실행 후 net start vmcompute 명령어를 입력한다.

pc 재부팅 후 Hyper-V 관리자에서 확인한다.



도커 명령어 사용 중 에러

```bash
the input device is not a TTY.  If you are using mintty, try prefixing the command with 'winpty'
```

이러한 에러가 발생할 경우 입력한 명령어 앞에 winpty를 입력해주면 정상적으로 실행된다.



## Vue 앱을 도커화 하기

뷰 앱이 정상적으로 동작하는지 확인해야 한다.

### 뷰 앱 정상구동 확인하기

뷰 앱의 루트 폴더에서 아래의 명령어를 입력하여 정상적으로 구동되는지 확인해 본다.

npm install

npm run serve



### 도커화

[공식 홈페이지](https://kr.vuejs.org/v2/cookbook/dockerize-vuejs-app.html) 참고

Vue 앱의 루트 폴더에서 Dockerfile을 생성한다(확장자 없음)

Dockerfile에 

```dockerfile
FROM node:lts-alpine

# install simple http server for serving static content
RUN npm install -g http-server

# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies leaving out dev dependencies
RUN npm install --production

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN npm run build

EXPOSE 8080
CMD [ "http-server", "dist" ]
```

이와 같이 입력해 준다.



그 다음 터미널에 아래의 명령어를 입력하여 front에 0.1태그를 달아 빌드한다.

docker build -t front:0.1



터미널에 아래의 명령어를 입력하여 서버를 구동시켜 본다.

docker run -it -p 8080:8080 --rm front:0.1

아이피 주소가 나올 것이다.

브라우저에서 아이피 주소:8080/ 를 입력하여 정상적으로 들어가지는지 확인한다.



## 스프링 부트 서버 도커화 하기

도커화 하기 전 서버가 정상 구동하는지 확인이 필요하다.

### 서버 구동 확인하기

백엔드 루트 폴더에서 터미널에 아래의 명령어를 입력한다.

./mvnw package

(mvnw 명령어를 사용하려면 vscode의 확장 프로그램 Java Extension Pack과 Spring Boot Extension Pack을 설치해야 한다.)



java에서 target/webcuration-0.0.1-SNAPSHOT.jar 파일을 실행하기 위하여 터미널에 아래의 명령어를 입력한다.

java -jar target/webcuration-0.0.1-SNAPSHOT.jar

### 도커화

[공식 홈페이지](https://spring.io/guides/gs/spring-boot-docker/) 참조



스프링 부트 서버 루트 폴더에 Dockerfile을 만들어 준다.

Dockerfile에 아래의 명령을 붙여넣고 저장한다.

```dockerfile
FROM openjdk:8-jdk-alpine
ARG JAR_FILE=target/*.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
```



아래의 명령어를 입력하여 빌드한다.

docker build . -t back:0.1



정상적으로 빌드가 되었다면 터미널에 아래의 명령어를 입력하여 스프링 부트 서버를 구동해 본다.

winpty docker run -it -p 8080:8080 --rm back:0.1

http://localhost:8080/swagger-ui.html#/ 주소를 입력하여 정상 구동여부 확인할 수 있다.



## DB 도커화 하기

docker에서 mysql db를 구축하려면 터미널에 아래의 명령어를 붙여넣는다.

```bash
docker run --name mysql -p 3307:3307 -e MYSQL_ROOT_PASSWORD=ssafyssafyroomroom -e MYSQL_DATABASE=ssafy -d mysql --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
```

password는 ssafyssafyroomroom이고 이름은 ssafy인 db가 만들어질 것이다.

아래의 명령어를 입력하여 mysql 이미지를 실행한다.

```bash
docker exec -it mysql mysql -uroot -p ssafy
```

비밀번호를 입력하면 정상 구동되는지 확인할 수 있다.



### 포트 충돌 시 대처방법

터미널에 netstat -ano 입력하여 포트 사용 상황을 본다

비어있는 포트를 찾아낸다.

이미 등록한 컨테이너를 삭제한다.

docker rm mysql

컨테이너 이름을 모르고 실행중이지 않은 경우

docker ps -a 를 입력하여 모든 컨테이너를 확인할 수 있다.

이전에 mysql 생성하던 명령어에서 포트 부분만 비어있는 포트로 할당해주면 된다.





### Dockerfile 주의사항

공식 홈페이지에 도커화 있는것을 그대로 붙여넣으면 안된다.

```dockerfile
# base image
FROM node:12.2.0-alpine

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /app/package.json
RUN npm install
RUN npm install react-scripts@3.0.1 -g

# start app
CMD ["npm", "start"]
```

내 경우에 이렇게 되어 있었으나, 경로에 app이 없어서 계속 오류가 발생하고 있었다. 이를 내 app 이름인 web으로 바꿔주고 나서야 정상적으로 빌드가 되었다.





## 도커 명령어

버전 확인

docker -v



테스트용 도커 컨테이너 실행

docker run hello-world



도커 컨테이너 실행하기

docker run -it -p 포트번호:포트번호 이미지이름:태그명

--rm 옵션을 넣어 주면 일회성 컨테이너를 생성한다.



모든 컨테이너 조회

docker ps -a



실행 중인 컨테이너만 조회하려면

docker ps



컨테이너 제거하려면

docker rm 컨테이너 이름 혹은 id



컨테이너 중지하려면

docker stop 컨테이너 이름 혹은 id



도커 이미지들 조회하려면

docker images



도커 이미지를 삭제하려면

docker rmi 이미지명:태그명 혹은 이미지 id

태그에 latest는 생략 가능하다



도커 이미지에 태그 추가하는 방법

docker tag front:0.1 front:latest

기존에 존재하는 front:0.1에서 복사해 와서 front:latest를 만들어 준다.



도커 이미지에서 태그 삭제하는 방법

docker rmi front:태그



모든 도커 컨테이너 중지

docker stop $(docker ps -a -q)



모든 도커 컨테이너 삭제

docker rm $(docker ps -a -q)



모든 도커 이미지 삭제

docker rmi $(docker images -q) 



## docker compose

