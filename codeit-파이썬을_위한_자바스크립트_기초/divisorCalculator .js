/*정수 n의 약수는 n을 나누었을 때 나누어떨어지는 수입니다. 
만약 정수 i가 정수 n의 약수라면, n을 i로 나누었을 때 나머지가 0이 나와야 하는 거죠.
while문을 활용해서 정수 n의 약수를 모두 출력하고, 
총 몇 개의 약수가 있는지 출력하는 프로그램을 작성해 보세요.*/



function divisorCalculator(n){
  let i = 1;
  let count =0;

  while (i<=n){
    if (n%i===0){
      console.log(i);
      count++;
    }
    i++;
  }
  console.log(`${n}의 약수는 총 ${count}개입니다.`)
}

divisorCalculator(180)