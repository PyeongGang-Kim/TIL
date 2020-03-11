import requests, json

def ans():
    global data
    data["yourAnswer"] = input()

def seturl():
    global url
    url = urlbase+res.json()['nextUrl']

r = []
data = {
    "nickname": "구미1반김평강",
    "yourAnswer":"1"
    }
urlbase = "http://13.125.222.176/quiz/"
idx = "jordan"
url = urlbase+idx
header = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }
tmp = ''
while 1:
    res = requests.post(url, data=json.dumps(data), headers=header)
    if res.status_code == 200:
        r.append(data["yourAnswer"])
        r.append(res.json())
        if res.json()['nextUrl'] == "수고하셨습니다.":
            break

        print(res.json()['question'])
        if res.json()['code'] == 600:
            print("오답입니다.")
            print(tmp)
            ans()
            continue
        seturl()
        ans()
        tmp = res.json()['question']
    else:
        print(res)
        ans()

for rr in r:
    print(rr)