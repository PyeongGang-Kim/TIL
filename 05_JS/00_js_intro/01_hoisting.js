/*
// Hoisting!
// 나중에 선언된 변수를 참조 할 수 있음
// 함수 or statement 최상단으로 올려지는 것(hoisting)
// 변수와 함수를 위한 메모리를 확보하는 과정
// 할당x 선언이 맨 위로 올라가고 할당안되면 undefined를 준다.
console.log(a)
var a = 10
console.log(a)


// var가 호이스트 되는 과정
// 1. 선언이 최 상단으로 올라감
var a
// 2. 이후 참조를 하려고 하면 에러가 나지 않고 undefined가 출력
// (TMI) JS 에서는 var 변수를 선언할 때 값을 넣어주지 않으면 undefined를 자동으로 넣어 줌
// 3. 할당은 그 뒤에 이루어짐
a = 10
// 4. 최종 출력
console.log(a)




console.log(b)
let b = 10
console.log(b)

// let이 호이스트 되는 과정
// 1. 선언이 최 상단으로 올라감
let b
// 2. 에러 발생
console.log(b)
// 3. 할당
b = 10
// 4. 출력
console.log(b)

// var 할당 과정
// 1. 선언 - 초기화 (동시에 진행) --> 처음에는 값이 없기 때문에 JS가 undefined를 할당
// 2. 값의 할당 진행

// let 할당 과정
// 1. 선언 -> 초기화 x
// 2. TDZ(Temporal Dead Zone) -> 임시적 사각지대
// 3. 초기화 (초기에는 값이 없기 때문에 undefined 할당)
// 4. 할당

let foo
let bar = undefined
console.log(foo)
console.log(bar)


x
let x = 1

// x가 할당되기 전에 접근해서 오류가 걸림


y
var y = 1
console.log(y)

// y가 할당되기 전에 접근했지만, 선언 시 undefined를 넣었기 때문에 오류 안생김
// 선언은 맨 위로 올라가기 때문.

if (x!== 1){
  console.log(y)
  var y = 3
  if (y===3) {
    var x = 1
  }
  console.log(y)
}

if (x===1) {
  console.log(y)
}

x = 7
console.log(x)


*/