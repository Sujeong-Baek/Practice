/** 조건문을 활용해서 키 140cm를 기준으로 탑승 가능 유무를 알려주는 checkHeight() 함수를 작성해 주세요. 
 * 키가 140이 넘으면 탑승이 가능합니다., 넘지 못하면 탑승이 불가능합니다.라고 출력돼야 합니다. */

// 파라미터 height을 활용하는 checkHeight 함수를 완성하세요
function checkHeight(height) {
  // 여기에 코드를 작성하세요
	if (height >= 140){
	  console.log("탑승이 가능합니다.");
	}else {
	  console.log("탑승이 불가능합니다.");
	}
}

// 테스트 코드
checkHeight(141);
checkHeight(135);
checkHeight(170);