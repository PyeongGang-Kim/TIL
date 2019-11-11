
// // primitive(원시)타입
// const a = 13
// const b = -5
// const c = 3.14
// const d = 2.998e8
// const e = Infinity
// const f = -Infinity
// const g = NaN   //not a number
// console.log(a, b, c, d, e, f, g)

// // string
// const sentence1 = 'Ask and go to the blue' // single
// const sentence2 = "Ask and go to the blue" // double
// const sentence3 = `Ask and go to the blue` // backtick
// console.log(sentence1, sentence2, sentence3)


// // 오류발생
// const word = "안녕
// 하세요"
// console.log(word)

// // 백틱은 줄 바꿈 또한 자연스럽게 인식한다. 변수도 넣을 수 있다.
// // 파이썬의 f스트링과 비슷함.
// // 이스케이프 문자열은 사용 불가능하다.
// const word = `안녕
// 하세요`
// console.log(word)


// //&{변수명}을 통해 변수를 불러올 수 있다.

// const age = 10
// const message = `홍길동은 ${age}
// 세입니다.`
// console.log(message)


// const happy = 'Will you join us?'
// const hacking = `Happy` + 'Hacking' + "!"
// console.log(happy, hacking)


// // boolean - 참, 거짓
// const truthy = true
// const falsy = false
// console.log(truthy, falsy)
// console.log(typeof truthy)
// console.log(typeof falsy)

// let frist_name
// console.log(frist_name)

// let last_name = null   //의도적으로 명시해준 것.
// console.log(last_name===null)

// console.log(typeof null)
// console.log(typeof undefined)
// console.log(null == undefined)
// console.log(null === undefined)

// console.log(!null)
// console.log(!undefined)

// let c = 0

// c+= 10
// console.log(c)
// c-=3
// console.log(c)
// c+=10
// console.log(c)
// c++
// console.log(c)
// c--
// console.log(c)

// // 비교 연산자
// console.log(3>2)
// console.log(3<2)

// console.log('A' < 'B')
// console.log('Z' < 'a')
// console.log('가' < '나')

// // 동등 비교 연산자(==)
// // 느슨한 평가. 사용 지양
// const a = 1
// const b = '1'
// console.log(a==b)
// console.log(a!=b)
// console.log(a==Number(b))

// // 자동 형변환 예시
// console.log(null*8) // 0
// console.log('5' -1) // 4
// console.log('5' +1) // 51(string)
// console.log('five'*2) // nan

// // 일치 연산자
// // 엄격한 평가
// const a=1
// const b='1'
// console.log(a===b) // false
// console.log(a===Number(b)) // true

// // 논리 연산자
// // and 연산
// console.log(true && false)  // false
// console.log(1 && 0) // 0
// console.log(0 && 1) // 0
// console.log(4 && 7) // 7
// // or 연산
// console.log(true || false) // true
// console.log(false || false) // false

// console.log(1||0) // 1
// console.log(0||1) // 1
// console.log(4||7) // 4

// // not
// console.log(!true) // false
// console.log(!false) // true

// // 삼항 연산자
// // 가장 앞의 boolean 값이 참이면 : 앞의 값이 반환되고 반대일 경우에는 : 뒤의 값이 반환
// console.log(true ? 1:2) // 1
// console.log(false?1:2) // 2

// // 삼항 연산의 결과를 변수에 할당 할 수 있다.
// const result = Math.PI > 4 ? "yep" : "nope" // nope
// console.log(result)