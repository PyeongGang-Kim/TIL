# SQL

사용자 환경변수에 sqlite를 저장한 경로를 작성해 준다.

shell에서 sqlite3 입력하면 쉘 실행된다.

종료하려면 (컨트롤z 후 엔터) 혹은 (.exit 입력 후  엔터)



```bash
<tutorial 이라는 데이터베이스 파일 만들기>
$ sqlite3 tutorial.sqlite3
SQLite version 3.29.0 2019-07-10 17:32:03
Enter ".help" for usage hints.
sqlite> .databases

main: D:\TIL\04_db\00_db_prac_1\tutorial.sqlite3

<csv모드 설정 후 hellodb.csv를 examples 테이블로 만든다.>
sqlite> .mode csv
sqlite> .import hellodb.csv examples

<examples 테이블의 모든 데이터 불러오기>
sqlite> SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-2424-1232

<보기 좋게 만들기 1. header를 보여주기>
sqlite> .headers on
sqlite> .mode column
```

```bash
<직접 classmates 테이블 만들기>
CREATE TABLE classmates (
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT
   ...> );  
```

```bash
<테이블 조회하기>
.tables
```

```bash
<테이블 정의 보기>
.schema 테이블이름
```

```bash
<테이블 제거하기>
DROP TABLE 테이블이름;
```

```bash
<데이터 추가하기>
INSERT INTO 테이블이름 (컬럼1, 컬럼2... ) VALUES (값1, 값2...)
```

```bash
<기본키, 제약 설정한 테이블 만들기>
CREATE TABLE classmates (
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT NOT NULL,
   ...> age INT NOT NULL,
   ...> address TEXT NOT NULL
   ...> );
```

```bash
<여러개의 값 한번에 넣기>
sqlite> INSERT INTO classmates (name, age, address) VALUES ('홍길동', 30, '서울')
   ...> ;
sqlite> SELECT * FROM classmates
   ...> ;
id          name        age         address
----------  ----------  ----------  ----------
1           홍길동         30          서울
sqlite> DROP TABLE classmates
   ...> ;
sqlite> .tables
examples
sqlite> CREATE TABLE classmates (
   ...> name TEXT NOT NULL,
   ...> age INT NOT NULL,
   ...> address TEXT NOT NULL );
sqlite> INSERT INTO classmates VALUES ('홍길동', 30, '서울'), ('김철수', 23, '대전'), ('
박나래', 23, '광주'), ('이요셉', 33, '구미');
sqlite> SELECT rowid, * FROM classmates;
rowid       name        age         address
----------  ----------  ----------  ----------
1           홍길동         30          서울
2           김철수         23          대전
3           박나래         23          광주
4           이요셉         33          구미
sqlite> SELECT * FROM classmates;
name        age         address
----------  ----------  ----------
홍길동         30          서울
김철수         23          대전
박나래         23          광주
이요셉         33          구미
```

```bash
<3개 가져오기>
sqlite> SELECT rowid, name FROM classmates LIMIT 3;
rowid       name
----------  ----------
1           홍길동
2           김철수
3           박나래
```

```bash
<조건 지정하기>
sqlite> SELECT name FROM classmates WHERE address='서울';
name
----------
홍길동
```

```bash
<중복 없이 가져오기>
SELECT DISTINCT age FROM classmates;
age
----------
30
23
33
sqlite>
```

```bash
<기본키, 제약 설정한 테이블 만들기(기본키는 삭제되고 나서도 사용되지 않는)>
CREATE TABLE tests (
   ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...> name TEXT NOT NULL,
   ...> age INT NOT NULL,
   ...> address TEXT NOT NULL
   ...> );

<1번 id를 삭제>
sqlite> DELETE FROM tests WHERE id=1;
<하나를 삽입>
sqlite> INSERT INTO tests (name) VALUES ('가나다라');
sqlite> SELECT * FROM tests;

id          name
----------  ----------
2           가나다
3           가나다라
sqlite>
```

```bash
<rowid = 4 인 레코드를 갱신하기>
sqlite> UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=4;
```

```bash
<레코드 갯수 세기>
SELECT COUNT(*) FROM users;
COUNT(*)
----------
COUNT, AVG, SUM, MIN, MAX 등을 쓸 수 있다.
```



WHERE column LIKE '';
2% 2로 시작하는 값
%2 2로 끝나는 값
%2% 2가 들어가는 값
_2% 아무 값이나 들어가고 두번째가 2로 시작하는 값
1___ 1로 시작하고 4자리인 값
2_%_% 2로 시작하고 적어도 3자리인 값



```bash
<LIKE 사용 20대인 사람(age첫째 자리가 2이고 한자리가 더 있는 사람)>
SELECT * FROM users WHERE age LIKE '2_';
```



```bash
<이름이 준으로 끝나는 사람>
sqlite> SELECT * FROM users WHERE first_name LIKE '%준';
```

```bash
<중간 번호가 5114인 사람>
SELECT * FROM users WHERE phone LIKE '%-5114-%';
```

```bash
<나이순 오름차순 10개만>
SELECT * FROM users ORDER BY age LIMIT 10;
```

```bash
<나이순 성 순 10개만>
SELECT * FROM users ORDER BY age, last_name LIMIT 10;
```

```bash
<계좌 잔액 내림차순 10개, 성 이름 가져오기>
SELECT last_name, first_name FROM users ORDER BY balance desc LIMIT 10;
```

```bash
<articles 테이블을 news로 이름 바꾸기>
ALTER TABLE articles RENAME TO news;
```

```bash
<date라는 DATETIME형식의 column을 추가하기>
ALTER TABLE news ADD COLUMN date DATETIME;

%% NOT NULL 속성을 넣으면 이미 있는 레코드들이 무결성을 위반하므로 안만들어진다.
따라서 1. NOT NULL 속성을 넣지 않고 만들거나, 2. 
```

```bash
<news 테이블의 date colume을 created_at으로 변경하기>
ALTER TABLE news RENAME date TO created_at;
```



테이블.objects.all().query

이런식으로 .query를 붙여주면 sql명령어를 볼 수 있다.