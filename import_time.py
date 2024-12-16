# 시간 관련 기능을 제공하는 모듈
import time
# 날짜 시간 데이터를 제공하는 모듈
import datetime

# 공부할 과목을 저장할 리스트
subjects = []

print("공부할 과목 입력 (종료: 'Q'):")
# while문을 써서 반복으로 과목 이름을 입력하게한다.
while True:
    # 사용자로부터 과목 이름을 입력받는다.
    subject = input("과목 이름: ")
    # 사용자가 원할 때 그만둘 수 있게 'Q'를 입력하면 break되게 한다.
    if subject == 'Q':  
        break
    # 사용자가 원하는 과목들을 하나의 리스트로 묶어야해서 사용했다. 
    subjects.append(subject) 

# 만약 리스트가 비어 있으면(길이가 0) 프로그램 종료 후 출력력
if len(subjects)==0:
    print("입력된 과목이 없습니다. 종료합니다.")
else:
    # 공부할 과목을 반복으로 출력하기 위해서 while문을 씀
    while True:
        print("\n공부할 과목 목록:")
        # 과목에 번호를 붙이기 위해 사용 ex) 1.수학 2.영어
        number = 1 
        # 반복문을 사용해서 리스트에 있는 과목과 number를 출력
        for subject in subjects: 
            print(f"{number}. {subject}")
            # 번호 증가
            number += 1  
        # 종료 표시
        print("0. 종료")  

        # 사용자로부터 번호 입력받음
        choice = input("\n번호 선택: ") 
        # choice를 숫자로 활용해야하기 때문에 정수형태로 바꿈.
        choice = int(choice)
        if choice == 0:  # 0을 선택하면 프로그램 종료
            print("프로그램을 종료합니다.")
            break
        
         # number에서 선택하도록 if문을 씀. else는 잘못된 번호라고 출력.
        if 1 <= choice <= len(subjects):
            # 선택한 과목을 보다 쉽게 출력하기 위해서 사용용
            choiced_subject = subjects[choice - 1] 
            print(f"\n'{choiced_subject}' 공부 시작. 중지: Ctrl+C")
            # 현재 시각을 start로 저장. 이유는 끝난 시간 - 시작한 시간 = 실시간으로 흐르는 시간이여서 
            start = time.time() 

            while True:
                # KeyboardInterrupt를 사용해 사용자가 원할 때 끝낼 수 있도록 하기 위해서 try문 사용
                try:
                    # 끝나는 현재 시간을 저장.
                    end = time.time() 
                    # 걸린 시간.
                    sec = (end - start)
                    times = str(datetime.timedelta(seconds=sec))

                    # 실시간으로 변동되는 타이머를 구현하고 싶어서 \r 과 end=" "를 사용용
                    print(f"\r진행시간: {times}",end=" ")
                    # 1초마다 시간을 최신화 시키고 싶어서 사용
                    time.sleep(1)  
                  
                except KeyboardInterrupt: 
                    print(f"\n'{choiced_subject}' 공부 완료.")
                    break
        else:
            print("잘못된 번호입니다.")  
