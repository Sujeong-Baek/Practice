/* 1
'number', 'string', 'boolean', 'null', 'undefined', 'array'가 순서대로 담겨있는 배열을 생성해 주세요.
배열의 두 번째 요소를 출력해 주세요.
배열의 마지막 요소를 출력해 주세요.
기본 자료형에 속하는 처음 5개 요소를 잘라내 주세요.*/

let dataTypes = [
  'number', 
  'string', 
  'boolean', 
  'null', 
  'undefined', 
  'array',
  ];

// 배열의 두 번째 요소를 출력해 주세요
console.log(dataTypes[1]);

// 배열의 마지막 요소를 출력해 주세요
console.log(dataTypes[dataTypes.length -1]);

// 기본 자료형에 속하는 처음 5개 요소를 잘라내서 출력해 주세요
console.log(dataTypes.slice(0,5));



/*2
반복문을 활용해서 배열에 있는 모든 요소를 하나씩 출력해 봅시다. */
let dataTypes2 = ['number', 'string', 'boolean', 'null', 'undefined', 'array'];

// 여기에 코드를 작성하세요
for (let i=0; i<dataTypes.length;i++){
  console.log(dataTypes[i])
}



//3 
let dataTypes3 = ['number', 'string', 'false', 'true', 'null', 'undefined'];

// 배열 끝에 'array'와 'object'를 추가해 주세요
// 여기에 코드를 작성하세요
dataTypes.push('array','object');
//dataTypes.splice(dataTypes.length-1,0,'array','object');
console.log(dataTypes);

// 배열의 마지막 요소 ('object')를 제거해 주세요
// 여기에 코드를 작성하세요
dataTypes.pop();
//dataTypes.splice(dataTypes.length-1,1);
console.log(dataTypes);

// 배열 중간에 있는 'false', 'true'를 제거해 주세요
// 여기에 코드를 작성하세요
dataTypes.splice(2,2);
console.log(dataTypes);

// 'string' 바로 다음에 'boolean'을 추가해 주세요
// 여기에 코드를 작성하세요
dataTypes.splice(2,0,'boolean');
console.log(dataTypes);



//4
let celsiusTemps = [27, 25, 26, 22, 28, 27, 21];
let fahrenheitTemps = []

// 여기에 코드를 작성하세요
for (let i=0;i<celsiusTemps.length;i++){
  fahrenheitTemps.push((celsiusTemps[i] * 9 / 5) + 32)
}

// 테스트 코드
console.log(fahrenheitTemps);