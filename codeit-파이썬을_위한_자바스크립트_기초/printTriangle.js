/*이번 실습은 아래와 같은 삼각형을 그려주는 함수를 구현하는 것입니다.

*
**
***
****

함수 이름은 printTriangle입니다.
함수는 삼각형 높이 height를 파라미터로 받습니다.
함수는 높이 height에 맞는 삼각형을 출력해 줍니다.
함수는 for문을 사용해야 합니다.

자바스크립트에서는 * 연산자를 문자열에 사용할 수 없습니다. 
대신 repeat()이라는 함수를 사용하면 됩니다. */

let star = '*';
console.log(star.repeat(4)); // ****
console.log('*'.repeat(4)); // ****

function printTriangle(height){
  for (let i=1; i<= height; i++){
    console.log('*'.repeat(i));
  }
}

// 테스트 코드
console.log('높이: 1');
printTriangle(1);

console.log('높이: 3');
printTriangle(3);

console.log('높이: 5');
printTriangle(5);