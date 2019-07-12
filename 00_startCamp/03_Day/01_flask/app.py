from flask import Flask
from datetime import datetime
import random

app=Flask(__name__)
@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/ssafy')
def ssafy():
    return 'This is ssafy'

@app.route('/dday')
def dday():
    today=datetime.now()
    endday=datetime(2019,11,29)
    td=endday-today
    return f"SSAFY 1학기 종료까지 {td.days}남았습니다."

@app.route('/html')
def html():
    return '<h1>This is HTML h1 tag</h1>'

@app.route('/html_line')
def html_line():
    return """
    <h1>여러 줄로 작성합니다.</h1>
    <ul>순서가 없는
        <li>1번</li>
        <li>2번</li>
    </ul>
    """
@app.route('/greeting/<string:name>')
def greeting(name):
    return f'반갑습니다! {name}님!'

@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 세제곱은 {number**3}입니다.'


# 점심 메뉴 리스트(5개)에서 2개 랜덤으로 뽑아 출력하기

@app.route('/lunch/<int:df>')
def lunch(df):
    lnc=['샌드위치', '쇠고기볶음', '빨간우동', '갈치카레구이', '프라이두부샐러드']
    rlnc=", ".join(random.sample(lnc,df))
    k=f'오늘의 점심메뉴 추천은 {rlnc}입니다.'
    return k