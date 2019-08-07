from django.shortcuts import render
from decouple import config
import json
import requests


# Create your views here.

def index(request):
    return render(request, 'utilities/index.html')

# 네이버 파파고 번역
def papago(request):
    return render(request, 'utilities/papago.html')

def translated(request):
    #1. 사용자가 입력한 번역하고자 하는 한국어 텍스트
    word = request.POST.get('word')
    #2. 네이버에 번역 요청을 위해 필요한 준비
    naver_client_id = config('NAVER_CLIENT_ID')
    naver_client_secret = config('NAVER_CLIENT_SECRET')
    #3. 요청을 보낼 url
    url = 'https://openapi.naver.com/v1/papago/n2mt' + 'source=ko&target=en&text=' + word
    headers = {'X-Naver-Client-Id': naver_client_id, 'X-Naver-Client-Secret': naver_client_secret}
    data={'source': 'ko', 'target': 'en' ,'text':word}
    result = requests.post('https://openapi.naver.com/v1/papago/n2mt',headers=headers,data=data).json().get('message').get('result').get('translatedText')



    
    context = {
        'word': word,
        'result': result,
    }
    return render(request, 'utilities/translated.html', context)