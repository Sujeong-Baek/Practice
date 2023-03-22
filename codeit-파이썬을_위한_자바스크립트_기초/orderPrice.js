/*
# 주문의 합계를 계산해 주는 함수
# burger, hotdog, drink는 각 아이템 개수를 뜻합니다.
def order_price(burger, hotdog, drink):
    burger_price = 6000
    hotdog_price = 5000
    drink_price = 3000

    total_price = burger * burger_price + hotdog * hotdog_price + drink * drink_price

    return total_price
*/

function orderPrice(buger, hotdog, drink){
  let bergerPrice = 6000;
  let hotdogPrice = 5000;
  let drinkPrice = 3000;

  let totalPrice = buger*bergerPrice + hotdog*hotdogPrice + drink*drinkPrice;

  return totalPrice;
}

console.log(orderPrice(1, 1, 2));//17000
console.log(orderPrice(0, 2, 2));//16000