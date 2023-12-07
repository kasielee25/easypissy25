function askForMore(change) {
    const result = confirm(`남은 잔액으로 음료를 한 번 더 선택하시겠습니까?`);
    
    if (result) {
        totalMoney += parseInt(document.getElementById('moneyInput').value); // 이전 금액을 저장
        displayAdditionalOptions(change); // 추가 음료 선택 함수 호출
    } else {
        const changeDisplay = document.getElementById('changeDisplay');
        const remaining = totalMoney + parseInt(document.getElementById('moneyInput').value); // 이전 금액을 포함한 전체 금액 계산
        changeDisplay.innerHTML = `현재 금액: 전체 금액<br>전체 금액: ${remaining}원`; // 전체 금액 표시
    }
}

function displayAdditionalOptions(change) {
    const drinkContainer = document.getElementById('drinkOptions');
    drinkContainer.innerHTML = '';

    // 이전에 선택한 음료 옵션을 계산하여 금액에서 제외
    const money = parseInt(document.getElementById('moneyInput').value) - change;

    // 추가 선택 가능한 음료 옵션 생성
    for (const [drink, price] of Object.entries(drinks)) {
        if (price <= money) {
            const drinkButton = document.createElement('button');
            drinkButton.classList.add('drink');
            drinkButton.textContent = `${drink}: ${price}원`;

            drinkButton.addEventListener('click', function() {
                selectAndDispenseDrink(drink, price);
            });

            drinkContainer.appendChild(drinkButton);
        }
    }
}
