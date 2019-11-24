# DB 시험

## 장고 orm

1. DB에 저장하는 방법

   1. 각 각의 값들을 직접 입력하는 방법.

      article = Article()

      article.title = 'title'

      article.content = 'content'

      article.save()

   2. 생성 할 때 기본값 넣는 방법

      article = Article(title='title', content='content')

      article.save()

   3. 바로 입력하는 방법

      Article.objects.create(title='title', content='content')

      

2. 유효성 검사

   저장 전 .full_clean()



3. 필터 사용법

   1. 조건이 하나일 때

      articles = Article.objects.filter(title='title')

   2. 조건이 두개 이상일 경우

      and 조건

      articles = Article.objects.filter(title='title').filter(content='content') 혹은

      articles = Article.objects.filter(title='title', contetn='content')

      or 조건

      articles = Article.objects.filter(title='title')|Article.objects.filter(content='content')

   3. 하나의 데이터를 가져올 때

      article = Article.objects.get(title='title')

      get의 경우 데이터가 없으면 오류가 발생한다. 또한 여러개를 받아도 오류가 발생한다.

      filter의 경우 데이터가 없어도 오류가 발생하지 않으며 쿼리 셋을 받기에 오류가 없다.

   4. 특수한 조건을 활용하는 방법

      ```bash
      __gt, __gte, __lt, __lte 
      크다 크거나 같다 작다 작거나 같다
      users.objects.filter(age__gt=30).count()
      
      __contains, __startswith, __endswith
      articles = Article.objects.filter(title__contains='fir')
      articles = Article.objects.filter(title__startswith='first')
      articles = Article.objects.filter(content__endswith='!')
      ```

      이처럼 칼럼에 언더바 두개 붙이고 contains, startswith, endswith의 명령어를 사용 가능하다.

4. 쿼리문을 보는 방법

   orm명령어 뒤에 .query를 붙이면 쿼리문을 볼 수 있다.



5. 값을 하나만 가져오는 두 번째 방법

   article = Article.objects.all()[0]

   0번 인덱스에 있는 객체 하나만 가져온다



6. 값을 슬라이싱을 통해 가져 올 수도 있다.

   article = Article.objects.all()[0:4]

   파이썬과 유사하게 동작한다. 하지만 -인덱스는 불가능하다.

   스텝 또한 넣을 수 있다.

   userlist = users.objects.all()[0:10:-3]

   음의 스텝의 경우에도 무조건 작은 수가 앞에 큰 수가 뒤에 나와야 한다.

   userlist = users.objects.all()[10:0:-3]

   이렇게 사용하면 아무것도 반환하지 않는다.



7. 업데이트 하는 방법

   객체를 하나 불러와서 해당 객체의 속성을 바꾼 후 저장해준다.

   ```python
   article = Article.objects.get(id=1)
   article.title = 'new title'
   article.save()
   ```



8. 삭제 하는 방법

   삭제도 업데이트와 마찬가지로 객체를 불러 온 후 삭제를 해 준다.

   ```python
   article = Article.objects.get(id=1)
   article.delete()
   ```

   

9. 전체 인원 수 세는 방법

   ```python
   Article.objects.all().count()
   ```

   

10. 정렬

    users.objects.order_by('balance', '-age')

    

11. 표현식의 사용(사용하기 위해서 from django.db.models import Avg, Count, Max, Sum, Min

    users.objects.filter(country='강원도').aggregate(Avg('balance'))

    users.objects.all().aggregate(Count('age', distinct=True))

    distinct 옵션은 유일성을 부여한다.. 하지만 Count에서만 사용 가능. Sum, Avg, Min, Max에선 사용되지 않는다.

    

    age의 합계 구하기

    users.objects.aggregate(Sum('age'))

    

    성이 황인 사람들의 age합계를 age로 그룹화 하여 보여주기

    users.objects.filter(last_name='황').values('age').annotate(Sum('age'))



12. 중개 모델

    ```python
    class Doctor(models.Model):
        name = models.TextField()
    
    class Patient(models.Model):
        name = models.TextField()
        doctors = models.ManyToManyField(Doctor, through='Reservation')
    
    class Reservation(models.Model):
        doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
        patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    ```

    through 옵션을 넣으면 p1.doctors.all()로 호출 가능하다.

    반대 가능하려면 related name을 넣어줄 것.

    예약 생성시에는 d2.patients.add(p2)

    삭제시에는 remove를 사용하면 된다.



## SQL

1. csv 파일로부터 불러오기

   .mode csv

   .import users.csv user  (users.csv에서 데이터 가져와 user테이블로)

2. 테이블 확인하기

   .tables

3. 스키마 확인하기

   .schema 테이블

4. 데이터베이스 확인하기

   .databases

5.  테이블 만들기

   create table 테이블명 (

   id INTEGER PRIMARY KEY,

   name TEXT

   );

6. 테이블 제거하기

   DROP TABLE 테이블명;

7. 데이터 추가하기(레코드)

   INSERT INTO 테이블명 (추가할 것들 몸무게, 키 등) VALUES (값 1, 값 2), (값 1, 값 2);

8. 중복 없이 데이터 가져 오기

   select distinct age from classmate

9. 데이터를 갱신하기

   update user set name='홍길동', address='제주도', where id=1001

10. like 사용법

    where phone like '_2%';

    _는 한 글자를, %는 0~무한개의 글자를 의미한다.

11. 테이블 명 바꾸기

    alter table 테이블명 rename to 새 테이블 이름

12. 칼럼 명 바꾸기

    alter table 테이블명 rename 칼럼명 to 새 칼럼 이름

13. 칼럼 추가하기

    alter table 테이블명 add column 칼럼명 형식명(datetime, integer 등) + 옵션(not null default 1)







DDL 데이터 정의어

CREATE, ALTER, DROP

DML 데이터 조작어

SELECT INSERT DELETE UPDATE

DCL 데이터 제어어(권한 설정)

REVOKE GRANE, ROLLBACK, COMMIT

