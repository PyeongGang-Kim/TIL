from flask import Flask, render_template, request
from decouple import config
import requests
app = Flask(__name__)
api_url='https://api.telegram.org'
chat_id=config('CHAT_ID')
token=config('TELEGRAM_BOT_TOKEN')
naver_client_id=config('NAVER_CLIENT_ID')
naver_client_secret=config('NAVER_CLIENT_SECRED')



@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text=request.args.get('message')
    requests.get(f'{api_url}/bot{token}/sendMessage?text={text}&chat_id={chat_id}')
    return render_template('send.html')


#텔레그램 서버에 제대로 받았다고 상태를 알려줌.
#200은 정상적으로 받았다는 메시지.
@app.route(f'/{token}', methods=['POST'])
def telegram():
    #1. 구조 print해보기& 변수 확인&저장
    print(request.get_json())
    print(type(request.get_json()))
    from_telegram=request.get_json()

    #2. 메시지를 그대로 돌려보내기
    if from_telegram.get('message') is not None:
        chat_id=from_telegram.get('message').get('from').get('id')
        text=from_telegram.get('message').get('text')
        #3. keyword(번역)
        if text[0:4]=='/번역 ':
            headers={'X-Naver-Client-Id': naver_client_id, 'X-Naver-Client-Secret': naver_client_secret}
            data={'source': 'ko', 'target': 'en' ,'text':text[4:]}
            resP=requests.post('https://openapi.naver.com/v1/papago/n2mt',headers=headers,data=data)
            print(resP)
            text=resP.json().get('message').get('result').get('translatedText')

        res=requests.get(f'{api_url}/bot{token}/sendmessage?chat_id={chat_id}&text={text}')
        
    return '',200
