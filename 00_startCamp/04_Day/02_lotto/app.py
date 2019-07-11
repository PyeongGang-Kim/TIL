from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests, random
app=Flask(__name__)

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
    num=request.args.get('num')#입력받은 데이터를 num에 저장

     #num회차의 로또api 에 접속해서 데이터를 받아와 딕셔너리로 반환(.json활용)
    lotto=requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}').json()  
    #. lotto 딕셔너리에서 번호 6개 가져오기
    winner=[]
    for i in range(1,7):
        winner.append(lotto[f'drwtNo{i}'])

    #2. 내 번호 리스트 만들기
    numbers=[]
    for num in request.args.get('numbers').split():
        numbers.append(int(num))
    print(numbers)
    if len(numbers) == 6:
        #번호 교집합 개수 찾기
        matched=0
        for num in numbers:
            if num in winner:
                matched+=1
        if matched==6:
            result='1등입니다'
        elif matched==5:
            if lotto['bnusNo'] in numbers:
                result ='2등입니다'
            else:
                result='3등입니다'
        elif matched==4:
            result='4등입니다'
        elif matched==3:
            result='5등입니다'
        else:
            result = '꽝입니다'
    else:
        result= '번호의 수가 6개가 아닙니다.'

    #lotto_result.html에 winner, numbers, result를 넘겨준다.
    return render_template('lotto_result.html', winner=winner, numbers=numbers, result=result)
