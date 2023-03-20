//1 Property Name: Property Value
let codethat = {
  name: '코드댓',
  bornYear: 2022,
  founder: {
    name: '김민준',
    age: 28
  },
	languages: ['C++', 'Java', 'JavaScript', 'Python'],
};

// name 프로퍼티 값을 출력해 주세요
console.log(codethat.name);
console.log(codethat['name']);

// founder의 name 프로퍼티 값을 출력해 주세요
console.log(codethat.founder.name);
console.log(codethat['founder']['name']);

// languages 프로퍼티의 3번째 값을 출력해 주세요
console.log(codethat.languages[2]);
console.log(codethat['languages'][2]);

// propertyName 변수를 이용해서 bornYear 프로퍼티 값을 출력해 주세요
let propertyName = 'bornYear';
console.log(codethat[propertyName]);



//2 영어단어장
let myVocab = {
  // 여기에 코드를 작성하세요
  function : '함수',
  variable : '변수',
  constant : '상수',
  'default value' : '기본 값',
  global : '세계적인',
};

// '지역의'라는 뜻을 가진 local 프로퍼티를 추가해 주세요
// 여기에 코드를 작성하세요
myVocab.local='지역의';
console.log(myVocab);

// global 프로퍼티의 값을 '전체적인'으로 바꿔 주세요
// 여기에 코드를 작성하세요
myVocab.global='전체적인';
console.log(myVocab);

// default value 프로퍼티를 삭제해 주세요
// 여기에 코드를 작성하세요
delete myVocab['default value']
console.log(myVocab);



//3 영어단어장2: object 안에 메소드
let myVocab = {
  function: '함수',
  variable: '변수',
  constant: '상수',
  global: '전체적인',
  local: '지역의',
  // 여기에 코드를 작성하세요
  printVocab: function (word){
    if (word in myVocab){
      console.log(`'${word}'의 뜻은 '${myVocab[word]}'입니다.`);
    } else{
      console.log('단어를 찾지 못했습니다.')
    }
  }
};

// 테스트 코드
myVocab.printVocab('function');
myVocab.printVocab('local');
myVocab.printVocab('array');