/**
main.py 파일을 보시면 파이썬으로 작성된 print_odd() 함수와 print_even() 함수가 있는데요. 
두 함수 모두 number라는 파라미터를 받습니다. 
print_odd() 함수는 0과 number 사이에 있는 모든 홀수를 출력하고 (0, number 포함) 
print_even() 함수는 0과 number 사이에 있는 모든 짝수를 출력합니다.
이 함수들을 자바스크립트 코드로 옮겨서 main.js 파일에 있는 printOdd() 함수와 printEven() 함수를 완성해 주세요.
 */
function printOdd(number) {
  for (let i=1; i <= number; i+=2){
    console.log (i);
  }
}

function printEven(number) {
  for (let i=0; i <= number; i+=2){
    console.log (i);
  }
}

// 테스트 코드
printOdd(10);
printOdd(23);
printEven(31);
printEven(18);