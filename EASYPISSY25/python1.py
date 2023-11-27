while True:
    # 입력 여부 물어보기
    user_input = input("입력하세요: ")
    
    # 입력한 내용 출력
    print("사용자 입력: ", user_input)

    # 프로그램 종료 여부 물어보기
    exit_question = input("프로그램을 종료하시겠습니까? (y/n): ")

    if exit_question.lower() == 'y':
        print("프로그램을 종료합니다.")
        break  # 루프를 종료하고 프로그램을 완전히 종료합니다.
    elif exit_question.lower() == 'n':
        print("프로그램을 계속 실행합니다.")
        # 여기에 프로그램을 계속 실행하는 코드를 추가할 수 있습니다.
    else:
        print("올바른 입력이 아닙니다. y 또는 n을 입력해주세요.")
