def calculator():
    while True:
        try:
            num1 = float(input("첫 번째 숫자를 입력하세요: "))
            operator = input("연산자를 입력하세요 (+, -, *, /): ")
            num2 = float(input("두 번째 숫자를 입력하세요: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            else:
                print("올바르지 않은 연산자입니다. 다시 시도하세요.")
                continue

            print(f"결과: {result}")

        except ValueError:
            print("올바른 숫자를 입력하세요.")

        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다.")

        again = input("계속해서 계산하시겠습니까? (y/n): ")
        if again.lower() != 'y':
            break

if __name__ == "__main__":
    calculator()
