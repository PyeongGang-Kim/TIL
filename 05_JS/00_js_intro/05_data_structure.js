/*
// Object & Array
// Array 음수 인덱스 불가. 시도하면 undefined반환
const numbers = [1, 2, 3, 4]
console.log(numbers[-1])
console.log(numbers.length)


// push

// pop
console.log(numbers.pop())
console.log(numbers)

// unshift 배열의 가장 첫번째 요소로 push 후 길이 리턴
console.log(numbers.unshift('a'))  //5
console.log(numbers) // a가 첫번째 요소로 push된 배열

// shift - 배열 가장 첫번째 요소를 제거하고 return
console.log(numbers.shift())
console.log(numbers)

// 복사본 혹은 다른값을 리턴
console.log(numbers.includes(1)) //numbers에서 1 이 포함되 있으면 true 아니면 false
console.log(numbers.includes(0)) //numbers에서 0이 포함되 있으면 true 아니면 false

console.log(numbers.push('a')) // 5
console.log(numbers.push('a')) // 6
console.log(numbers)
console.log(numbers.indexOf('a')) // 앞에서부터 a를 찾아보며 그 인덱스를 넘겨줌 없으면 -1리턴
console.log(numbers.indexOf('b')) // 앞에서부터 b를 찾아보며 그 인덱스를 넘겨줌 없으면 -1리턴

// join -
console.log(numbers.join()) // 아무것도 안 넣으면 ,로 구분지어줌
console.log(numbers.join('-')) // 넣은 문자열로 엮어줌

// 배열의 원본은 변하지 않음
console.log(numbers)




const me = {
  name: 'ssafy',
  'phone number': '0101234568',
  appleProducts: {
    ipad: '2018pro',
    iphone: '6s+',
    macbook: '2018pro'
    }
}

const books = ['사서삼경', '천자문']
const movies = {
  'Horror': ['곤지암', '겟아웃'],
  'SF': ['인셉션', '마션', '인터스텔라', '그래비티']
}

///es5
const magazines = null
const bookShop = {
  books: books,
  movies: movies,
  magazines: magazines,
}

console.log(bookShop)
console.log(typeof bookShop)
console.log(bookShop.books[1])




const me = {
  name: 'ssafy',
  'phone number': '0101234568',
  appleProducts: {
    ipad: '2018pro',
    iphone: '6s+',
    macbook: '2018pro'
    }
}

const books = ['사서삼경', '천자문']
const movies = {
  'Horror': ['곤지암', '겟아웃'],
  'SF': ['인셉션', '마션', '인터스텔라', '그래비티']
}

///es6 이상
// books: books, 이런것처럼 똑같은 경우엔 그냥 books, 로 입력해도 된다.


const magazines = null
const bookShop = {
  books,
  movies,
  magazines,
}

console.log(bookShop)
console.log(typeof bookShop)
console.log(bookShop.books[1])


*/


// JSON <-> Object
// JSON -> JS의 Object 형태와 유사한 문자열!!
// 실제 모습만 비슷하고 JS Object로 사용하기 위해서는 변환이 필요하다.

// Object -> String(json)
const jsonData = JSON.stringify({
  coffee: 'Americano',
  iceCream: 'Cookie and cream'
})
console.log(jsonData)
console.log(typeof jsonData)


// String -> Object
const parseData = JSON.parse(jsonData)
console.log(parseData)
console.log(typeof parseData)


// Object와 JSON의 차이
// Object: JS의 Key-Value pair의 자료 구조
// JSON: JS의 Object와 비슷하게 생긴 단순 스트링
