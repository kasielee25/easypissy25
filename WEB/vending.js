// 음료수 목록 및 가격 설정 (자판기 인스턴스와 동일하게 설정해주세요)
const drinks = {
    '2%': 1300,
    '삼다수': 900,
    '제로콜라': 1500,
    '나랑드': 1100,
    '데미소다': 1000,
    '환타': 1200
};

// HTML 페이지에 음료 옵션 표시하는 함수
function displayOptions() {
    const money = parseInt(document.getElementById('moneyInput').value);
    const drinkContainer = document.getElementById('drinkOptions');
    drinkContainer.innerHTML = '';

    for (const [drink, price] of Object.entries(drinks)) {
        if (price <= money) {
            const drinkDiv = document.createElement('div');
            drinkDiv.classList.add('drink');
            drinkDiv.textContent = `${drink}: ${price}원`;

            drinkDiv.addEventListener('click', function() {
                // 음료를 클릭하면 해당 음료 선택
                selectAndDispenseDrink(drink);
            });

            drinkContainer.appendChild(drinkDiv);
        }
    }
}

// 음료 선택 및 제공하는 함수
function selectAndDispenseDrink(selectedDrink) {
    const money = parseInt(document.getElementById('moneyInput').value);
    console.log(`선택한 음료: ${selectedDrink}`);
    console.log(`넣은 돈: ${money}`);
}

// 돈 입력 시 음료 목록을 표시하는 이벤트 리스너 등록
document.getElementById('moneyInput').addEventListener('input', displayOptions);
