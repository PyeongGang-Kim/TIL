// // JS에서는 아래의 3가지 조건을 만족하기 때문에 1급 객체(first class object)다
// // 1. 변수에 담을 수 잇다.
// // 2. 인자로 전달 할 수 있다.
// // 3. 반환값(return)으로 전달할 수 잇다.

// const fco = function() {
//   return n => n+1
// }

// console.log(fco)

// // 도전과제 -> num_101 변수에 101을 담아야 한다.(fco함수를 활용))
// const num_101 = fco()(100)
// console.log(num_101)


// // 3초 후 출력
// setTimeout(function(){
// 	console.log('3초 후 출력된다')
// }, 3000)



// // 알림창 출력
// function doSomething(subject) {
//   alert(`자 이제 ${subject} 과목 평가 준비 좀 시작해볼까???`)
// }
// doSomething('django')

// // 알림창 연속으로 출력
// function doSomething(subject, callback) {
//   alert(`자 이제 ${subject} 과목 평가 준비 좀 시작해볼까???`)
// callback()
// }
// doSomething('django', function(){
// alert(`내일이 시험인데??`)
// })


// function alertFinished(){
//   alert('내일이 시험인데??')
// }
// doSomething('django', alertFinished)



// document.querySelector('.bg')
// 를 하면
// <div class=​"bg">​…​</div>​
// 이 출력된다.


// document.querySelectorAll('.bg')
// 를 하면
// NodeList(2) [div.bg, div.bg]
// 이 출력된다


// const bg = document.querySelector('.bg')

// const dino = bg.querySelector('#dino')
// // dino 이미지를 선택할 수 있다.


// // 스타일들을 조회해 보기
// dino.style

// // 스타일을 바꿀 수도 있다.
// dino.width = '500px'

// // 제거할 수도 있다.
// dino.remove()


// // 객체를 넘겨서 삭제할 수도 있다.
// const bg = document.querySelector('.bg')
// const dino = document.querySelector('#dino')
// bg.removeChild(dino)


// // 객체를 추가하는 방법
// // 이미지 객체를 만든다.
// const newDino = document.createElement('img')
// // 이미지 객체에 속성을 입력한다
// newDino.src = 'url'
// newDino.alt = 'dino'
// newDino.id = 'dino-1'
// newDino.style.width='100px'
// // 추가할 곳을 선택한다
// const bg = document.querySelector('.bg')
// // 추가할 곳에 객체를 append한다
// bg.append(newDino)


// p태그를 만들고
const p = document.createElement('p')
// document에 추가
document.body.appendChild(p)
// 태그 안에 내용을 추가
p.innerHTML = '<b>다이노 귀엽다</b>'
