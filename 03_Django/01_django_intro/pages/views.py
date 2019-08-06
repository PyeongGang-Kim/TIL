from django.shortcuts import render
import random
from datetime import datetime
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def introduce(request):
    return render(request, 'introduce.html')

def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick': pick}
# dinner.html에서 사용할 pick, views에서의 pick
    return render(request, 'dinner.html', context)
    #세번째 값은 선택사항인데 딕셔너리만 들어갈 수 있다.

def image(request):
    return render(request, 'image.html')

#이렇게 직접 딕셔너리를 넣어 줘도 된다.
#    return render(request, 'dinner.html', {'pick': pick})


#3. Variable Routing(동적 라우팅)
def hello(request, name, age):
    # names = ['justin', 'john', 'jason', 'juan', 'zzulu']
    # name = random.choice(names)
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {
        'name': name,
        'age': age, 
        'pick': pick,
    }
    return render(request, 'hello.html', context)

#4. 실습
#4-1. 동적 라우팅을 활용해서(name과 age를 인자로 받아) 자기소개 페이지
def prod(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'prod.html', context)

#4-2. 두개의 숫자를 인자로 받아(num1, num2) 곱셈 결과를 출력
def product(request, num1, num2):
    context = {
        'result': num1*num2,
    }
    return render(request, 'product.html', context)

#4-3. 반지름(r)을 인자로 받아 원의 넓이(area)를 구하시오
def area(request, r):
    context = {
        'area': r**2*3.14,
    }
    return render(request, 'area.html', context)

#5. DTL(Django Template Language)
def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']

    empty_list = ['14']
    datetimenow = datetime.now()


    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }

    return render(request, 'template_language.html', context)

#6. 실습
#6-1. isbirth
def isbirth(request, month, day):
    today = datetime.now()
    if today.month == month and today.day == day:
        result = True
    else:
        result = False
    context = {
        'result': result
    }
    return render(request, 'isbirth.html', context)
#6-2. 회문판별
def ispal(request, word):
    if word == word[::-1]:
        result = True
    else:
        result = False
    context = {
        'result': result
    }
    return render(request, 'ispal.html', context)
#6-3. 로또 번호 추첨
# lottos -> 1,45까지의 번호 중 6개를 랜덤으로 pick한 리스트
# real_lottos -> [21 24 30 32 40 42]
# 1. DTL(for문) 문법을 활용해 하나씩 출력 해보기 (lottos)
# 2. 컴시기가 뽑은 로또 번호와 실제 로또 당첨 번호를 비교해보기(DTL-if문)

def islotto(request):
    lottos = sorted(random.sample(list(range(1,46)), 6))
    real_lottos = [21, 24, 30, 32, 40, 42]
    result = lottos == real_lottos

    context = {
        'lottos': lottos,
        'real_lottos': real_lottos,
        'result': result,
    }


    return render(request, 'islotto.html', context)

def throw(request):
    
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {
        'message': message,
        'message2': message2
    }
    return render(request, 'catch.html', context)


def ping(request):
    return render(request, 'ping.html')

def pong(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {
        'message': message,
        'message2': message2,
    }
    return render(request, 'pong.html', context)

#8. Form - GET 실습(아스키 아티)
def art(request):
    return render(request, 'art.html')

def result(request):
    #1. form으로 날린 데이터를 받는다.(GET)
    word = request.GET.get('word')

    #2. ARTII api로 요청을 보내 응답 결과를 fonts에 저장한다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text

    #3. str을 list로 변경
    fonts = fonts.split('\n')

    #4. fonts(list)안에 들어있는 요소 중 하나를 선택해서 font라는 변수에 저장
    font = random.choice(fonts)

    #5. font를 가지고 요청을 보내어 받은 결과를 result에 저장한다.
    result = requests.get('http://artii.herokuapp.com/make?text=' + word + '&font=' + font).text
    context = {
        'result': result,
    }
    return render(request, 'result.html', context)

def user_new(request):
    return render(request, 'user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {
        'name': name,
        'password': pwd,
    }
    return render(request, 'user_create.html', context)