class VendingMachine:
    def __init__(self):
        # 음료수 목록 및 가격 설정
        self.drinks = {'2%': 1300, '삼다수': 900, '제로콜라': 1500, '나랑드': 1100, '데미소다': 1000, '환타': 1200}

    def display_options(self, available_drinks=None):
        print("======음료수 목록=========")
        drinks_to_display = available_drinks if available_drinks else self.drinks
        for drink, price in drinks_to_display.items():
            print(f"*{drink}: {price}원")

    def select_drink(self, money):
        # 가장 저렴한 음료수의 가격 확인
        min_price = min(self.drinks.values())

        # 돈이 가장 저렴한 음료수의 가격보다 작은지 확인
        if money < min_price:
            print("돈이 부족합니다. 더 많은 돈을 넣어주세요.")
            return

        remaining_change = money  # 남은 거스름돈 초기화

        while remaining_change >= min_price:
            # 선택 가능한 음료수 목록 구하기
            available_drinks = {drink: price for drink, price in self.drinks.items() if price <= remaining_change}

            # 음료수 목록 표시
            self.display_options(available_drinks)

            # 사용자로부터 음료수 선택
            selected_drink = input("""==========================
뽑을 음료수를 선택하세요: """)

            # 선택한 음료수가 유효한지 확인
            if selected_drink in available_drinks:
                # 음료수 제공
                print(f"""{selected_drink}이(가) 나왔습니다. Enjoy!
""")

                # 거스름돈 계산
                remaining_change -= self.drinks[selected_drink]
                if remaining_change > 0:
                    print(f"▶ 남은 거스름돈 <{remaining_change}>원으로 더 뽑을 수 있습니다.")
                # 사용자에게 추가적인 선택 여부 묻기
                continue_choice = input("더 음료수를 뽑으시겠습니까? (y/n): ")
                if continue_choice.lower() != 'y':
                    print("자판기 프로그램을 종료합니다.")
                    break
            else:
                print("올바르지 않은 음료수 선택입니다.")

        if remaining_change < min_price:  # 남은 거스름돈이 선택 가능한 음료수의 가격보다 작은 경우
            print("돈이 부족합니다!!!!!!!!")

# VendingMachine 인스턴스 생성
vending_machine = VendingMachine()

# 무한 루프
while True:
    # 사용자로부터 돈 입력 받기
    money_input = input("돈을 넣어주세요 (종료하려면 0 입력): ")

    # 종료 조건 확인
    if money_input == '0':
        print("자판기 프로그램을 종료합니다.")
        break

    # 입력값이 숫자인지 확인
    if not money_input.isdigit():
        print("올바른 숫자를 입력해주세요.")
        continue

    # 입력값을 정수로 변환
    money = int(money_input)

    # 음료수 선택
    vending_machine.select_drink(money)
