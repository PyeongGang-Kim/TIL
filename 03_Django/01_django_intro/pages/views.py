from django.shortcuts import render
import random
from datetime import datetime

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

    empty_list = ['ㅣ']
    datetimenow = datetime.now()


    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }

    return render(request, 'template_language.html', context)