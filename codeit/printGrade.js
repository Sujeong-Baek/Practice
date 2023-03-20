/**학생들에게 최종 성적을 알려 주는 '학점 계산기'를 만들려고 합니다.
이 수업에는 50점 만점의 중간고사와 50점 만점의 기말고사가 있어요. 
두 시험의 점수를 합해서 최종 성적을 내는 방식입니다. 규칙은 다음과 같습니다.
A: 90점 이상
B: 80점 이상 90점 미만
C: 70점 이상 80점 미만
D: 60점 이상 70점 미만
F: 60점 미만 */

function printGrade(midtermScore, finalScore){
  let total= midtermScore + finalScore;
  if (total>=90){
    console.log("A");
  } else if (80<=total && total<90){
    console.log("B");
  } else if (70<=total && total<80){
    console.log("C");
  } else if (60<=total && total<70){
    console.log("D");
  } else {
    console.log("F");
  }
}

// 테스트 코드
printGrade(25, 35);
printGrade(50, 45);
printGrade(29, 24);
printGrade(37, 42);