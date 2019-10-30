# Java Script

## 기본 세팅

nodejs를 검색해서 다운로드 후 설치

vscode 터미널에서 node 타이핑햇을때 들어가지면 설치 제대로 됨

extension에 Live Server, Auto Close Tag, Rainbow Brackets, indent-rainbow, Beautify



에디터 탭 사이즈를 4에서 2로 바꾼다.

f1누르고 preference쳐서 settings.json에 들어가 파이썬부분을 추가한다.

```json
{
    "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe",
    "editor.mouseWheelZoom": true,
    "workbench.startupEditor": "newUntitledFile",
    "workbench.iconTheme": "vscode-icons",
    "[python]": {
        "editor.tabSize": 4
    },
    "editor.tabSize": 2
}
```

File Preference Setings에서 Editor: tab Size = 2





var는 ex6이전에 나왔던 선언방법이다. 권장하지 않음

let은 선언 딱 한번만가능. 할당은 자유롭게 할 수 있다.

const는 할당과 선언 딱 한번만 가능. 할당이 되고 난 후에 재할당은 불가능하다.



브라우저 콘솔에서

const userName = prompt('Hello! Who are you?') 를 입력하면

입력 창이 하나가 뜬다

거기에 입력한 값이 userName에 저장이 된다.



```js
const userName = prompt('Hello! Who are you?')
undefined
userName
"ssw"
let message = ''
undefined
switch(userName){
    case '1q2w3e4r': {
        message = '<h1>This is secret admin page.</h1>'
    }
    case 'ssafy':{
        message = '<h1>You are from matrix.</h1>'
    }
    default:{
        message = `<h1>Hello ${userName}.</h1>`
    }
}
"<h1>Hello ssw.</h1>"
document.write(message)
undefined
```



```js
switch(userName){
    case '1q2w3e4r': {
        message = '<h1>This is secret admin page.</h1>'
		console.log(message)
		break
    }
    case 'ssafy':{
        message = '<h1>You are from matrix.</h1>'
		console.log(message)
		break
    }
    default:{
        message = `<h1>Hello ${userName}.</h1>`
		console.log(message)
    }
}
```

