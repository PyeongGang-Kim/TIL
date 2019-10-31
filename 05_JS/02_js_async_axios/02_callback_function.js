// // 배열로 이루어진 숫자들을 다 더하는함수

// // 배열로 이루어진 숫자들을 다 빼는 함수

// // 벼올로 이루어진 숫자들을 다 곱하는 함수
// const numberAddEach = numbers => {
//   let sum = 0
//   for (const number of numbers) {
//     sum += number
//   }
//   return sum
// }
// console.log(numberAddEach([1,2,3,4,5]))


// const numberSubEach = numbers => {
//   let sum = 0
//   for (const number of numbers) {
//     sum -= number
//   }
//   return sum
// }
// console.log(numberSubEach([1,2,3,4,5]))


// const numberMulEach = numbers => {
//   let sum = 1
//   for (const number of numbers) {
//     sum *= number
//   }
//   return sum
// }
// console.log(numberMulEach([1,2,3,4,5]))


// const NUMBERS = [1, 2, 3, 4, 5]
// const numbersEach = (numbers, callback) => {
//   let acc
//   for (const number of numbers){
//     acc = callback(number, acc)
//   }
//   return acc
// }

// // 더한다
// const addEach = (number, acc=0) => {
//   return acc+number
// }

// // 뺀다
// const subEach = (number, acc=0) => {
//   return acc-number
// }

// // 곱한다
// const mulEach = (number, acc=1) => {
//   return acc*number
// }
// console.log(numbersEach(NUMBERS, addEach))
// console.log(numbersEach(NUMBERS, subEach))
// console.log(numbersEach(NUMBERS, mulEach))



// 마지막 리팩토링
const NUMBERS = [1, 2, 3, 4, 5]
const numbersEach = (numbers, callback) => {
  let acc
  for (const number of numbers){
    acc = callback(number, acc)
  }
  return acc
}

console.log(numbersEach(NUMBERS, (number, add=0) => add + number))
console.log(numbersEach(NUMBERS, (number, add=0) => add - number))
console.log(numbersEach(NUMBERS, (number, add=1) => add * number))
