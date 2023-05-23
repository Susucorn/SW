'''
2023.05.23
박수연

# 문제정의
    stu.txt파일을 읽어서 각 학생의 평균 성적 계산해서 출력

# 문제분석
    변수 - 한줄씩 읽어서 저장 (score), 리스트 자료로 변환 (scorelist), 리스트에서 이름 항목 저장 (name), 세 과목의 합계 (sum)

# 알고리즘
    1. 파일 열기 - 읽기 모드
    2. 파일 처리 
        반복문 (while True :)
            한 줄 읽어서 score에 저장
            선택 (if score=='')
                반복 종료
            읽어온 내용을 리스트로 변환, scorelist에 저장
            scorelist에서 첫번째 항목을 name 에 저장 (이름)
            
            반복문 (for i in range(1,4): )
                scorelist의 1,2,3 항목의 값을 sum에 더해서 저장
    3. 파일 닫기
'''

f=open("c:/data/stu.txt",'r') #읽기모드로 파일 객체 생성
while True: # 무한반복
    score=f.readline()  # 한 줄씩 읽어오기
    if score=='':    # 더 이상 읽은 내용이 없다면
        break        # 반복 종료
    
    scorelist=score.split() # .split(), 문자열을 공백을 기준으로 분리하여 리스트 자료로 바꿔주는 함수
    name=scorelist[0]       # 리스트 첫번째 항목은 name(이름) 에 저장 , 리스트는 0번째부터 시작

    sum=0   # 합계를 저장해야하기 때문에 0으로 초기화
    for i in range(1,4):    # 1,2,3까지 저장
        sum=int(scorelist[i])    # i의 두번째 값 저장, 세번째 값 저장, 네번째 값 저장 (합계),   리스트 자료형에서는 숫자도 문자열로 인식하기 때문에 정수로 바꿔주기

    print(name,"의 평균 성적은 :%.1f"%(sum/3))
f.close()   # 파일닫기