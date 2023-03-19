/*
문 구분	; 사용
함수, 변수 이름	카멜 케이스 사용
변수 선언	let
함수 선언	function { ... }
리턴 문	return
사칙연산	+, -, *, / (파이썬과 동일)
한 줄 코멘트	//
여러 줄 코멘트	 /* … */


/*
[수학 연산]
대부분의 수학 연산은 파이썬과 완전히 똑같습니다. 
유일한 예외 케이스는 파이썬의 버림 나눗셈(//)
자바스크립트에는 버림 나눗셈이 따로 없습니다. 
//는 버림 나눗셈이 아닌 코멘트로 인식되니까 유의

console.log(3 // 2); // //가 코멘트로 인식됨

*/



/*
[증가, 감소 연산자]
파이썬에는 없는 연산자 
1을 증가하거나 감소할 때는 더 간결하게 ++와 --를 사용
*/
let i = 5;

i++; // i += 1과 똑같음
console.log(i); // 6

i--; // i -= 1과 똑같음
console.log(i); // 5


/*
문자열(String)
선언
파이썬처럼 큰따옴표(")를 사용해도 되고,
작은따옴표(')를 사용해도 됩니다.
*/
/* 큰따옴표 */
let str1 = "Hello World!";

/* 작은따옴표 */
let str2 = 'Hello World';


/*
문자열 포매팅 (템플릿 문자열)
파이썬에서는 str.format() 또는 f-string을 사용해서 문자열 사이사이에 변숫값을 넣었는데. 
자바스크립트도 비슷한 문법
문자열을 백틱(`) 기호로 선언하고, 변수를 ${}로 감싸주면 됩니다.
*/
let name = "서준"
let greeting = `안녕하세요 ${name} 님!`;
console.log(greeting); // 안녕하세요 서준 님!

let ii = 8;
let j = 13;
let message = `${ii} 더하기 ${j}는 ${ii + j}입니다.`;
console.log(message); // 8 더하기 13은 21입니다.


/*
특수 문자열
특정 문자들은 그대로 입력하면 안 되고 특수 문자열을 사용 
파이썬에서는 줄바꿈(\n), 작은따옴표(\'), 큰따옴표(\") 같은 것들
자바스크립트도 똑같은 특수 문자열을 사용

\n	줄바꿈
\t	탭
\'	작은따옴표
\"	큰따옴표
\\	백슬래시

*/


/*
불린형(Boolean)
불린형은 참(true)과 거짓(false) 둘 중 하나의 값을 가지는 데이터

선언
자바스크립트에서는 true와 false에 소문자를 사용
*/
let x = true;
let y = false;


/*
비교 연산자
파이썬과 비슷하지만 일치, 불일치는 등호 기호를 하나 더 씁니다.

파이썬: ==, !=
자바스크립트 ===, !==
*/
console.log(3 === 3); // true
console.log(3 !== 3); // false
console.log('Codeit' === 'Codeit'); // true
console.log('Codeit' === 'Codeeat'); // false


/*
===과 ==
== 연산자는 자동으로 형 변환(type conversion)을 해줍니다.
자동으로 형 변환을 해주면 편한 면도 있지만, 
언제 형 변환을 해주는지, 어떻게 변환을 해주는지를 정확히 이해하고 있지 못하면 
예상치 못한 결과가 나올 수 있기 때문에 ===을 사용하시는 걸 추천.
*/

/* == */
console.log('3' == 3); // true

/* === */
console.log('3' === 3); // false



/*
자바스크립트에서도 불린 값을 조합할 수 있는데, 
and, or, not 단어 대신 &&, ||, ! 기호를 사용*/

/* 두 값이 모두 참이어야 참 */
console.log((1 < 2) && (3 === 3)); // true
console.log((2 < 1) && (3 === 3)); // false

/* 두 값 중 하나만 참이어도 참 */
console.log((1 < 2) || (3 === 3)); // true
console.log((2 < 1) || (3 === 3)); // true

/* 값 부정 */
console.log(! (1 < 2)); // false
console.log(! (2 < 1)); // true



/*
형변환
숫자형으로 : Number()
문자열로 : String()
불린형으로 : Boolean()


자바스크립트에서 값이 'truthy'하다는 건, 
불린형으로 변환했을 때 값이 true라는 뜻이고, 
'falsy'하다는 건, 
불린형으로 변환했을 때 값이 false라는 뜻입니다. 
falsy한 값 0 (숫자 0), '' (빈 문자열)
*/



/*
null은 값이 없다는 걸 의도적으로 표현할 때 사용
undefined는 코드를 실행했는데 값이 없을 경우 사용
코드를 보면 codeit이라는 변수에는 값이 없습니다. 
아직 값이 할당되지 않은 것이지, 
'codeit은 값이 없다 (빈 값이다)'라고 선언하지는 않았습니다. 
그래서 codeit의 값은 undefined가 되는 겁니다.

null, undefined 둘 다 falsy하다.*/

let codeit;
console.log(codeit); //undefined

