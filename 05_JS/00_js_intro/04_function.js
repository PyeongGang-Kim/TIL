
// // Function
// // 선언식
// function add(num1, num2) {
//   return num1 + num2
// }
// console.log(add(2, 7))

// // 표현식
// const sub = function(num1, num2){
//   return num1-num2
// }
// console.log(sub(7, 2))

// // js에서는 함수도 하나의 값
// console.log(typeof add)
// console.log(typeof sub)

// // Arrow function (화살표 함수)
// // why arrow function?
// // 화살표 함수는 항상 익명 함수
// // function keyword 생략 가능
// // 함수의 매개변수가 1개라면 () 생략 가능
// // 함수 바디의 표현식이 하나라면 {}와 return 생략 가능

// // 함수 표현식
// const ssafy1 = function() {
//   return 'Hello'
// }
// console.log(ssafy1())


// // 화살표 함수로 바꿔보기
// // function 키워드를 삭제할 수 있음.
// const ssafy1 = (name) => { return `hello ${name}` }
// console.log(ssafy1('justin'))
// // 괄호를 생략할 수 있다. (인자가 1개뿐일때)

// const ssafy1 = name => { return `hello ${name}` }
// console.log(ssafy1('justin'))
// // 중괄호와 return도 생략할 수 있다. (표현식이 하나일 경우)
// const ssafy1 = name => `hello ${name}`
// console.log(ssafy1('justin'))

// let square = function(num){
//   return num ** 2
// }
// let num = 3
// console.log(square(num))
// square = (num) => {return num**2}
// console.log(square(num))
// square = num => {return num**2}
// console.log(square(num))
// square = num => num**2
// console.log(square(num))

// // 4. 인자가 없을 때 -> (), _ 표현 가능
// let noArgs = () => 'No args'
// console.log(noArgs())
// noArgs = _ => 'No args'
// console.log(noArgs())


// // 5-1. object 리턴하려고 한다면?
// let returnObject = () => {return {key:'value'}}
// console.log(returnObject())
// console.log(typeof returnObject())

// // 5-2 return을 적지 않으려면 괄호를 활용.{return  }을 (   )로 변경
// returnObject = () => ( { key: 'value'})
// console.log(returnObject())
// console.log(typeof returnObject())

// // 5-3 return을 적지 않았을 때
// returnObject = () => { key: 'value'}
// console.log(returnObject())
// console.log(typeof returnObject())


// // 기본 인자를 줄 때는 인자 갯수와 상관없이 괄호를 꼭 해야 한다.
// // 괄호가 없으면 systax error 발생
// const sayHello = (name='noName') => `hi ${name}`
// console.log(sayHello('justin'))
// console.log(sayHello())


// // 원래 함수에는 이름이 있다. function cube () {}
// // 익명함수/1회용 함수 -> 변수에 담아서 사용
// const cube = function(num) {return num**3}
// const squareRoot = num => num ** 0.5
// console.log(cube(2))
// console.log(squareRoot(4))


// // 즉시 실행 함수->주로 초기화에 많이 사용
// console.log((function (num) { return num**3})(2))
// console.log((function (num) { return num**0.5})(4))



// // 함수 호이스팅. 선언 전에 사용해도 괜찮다.
// // 하지만 변수에 저장한 함수는 선언 전에 호출 되면 안된다.

// ssafy()
// function ssafy(){
//   console.log('hoisting')
// }

// ssafy2()
// let ssafy2 = function(){
//   console.log('hoisting')
// }


