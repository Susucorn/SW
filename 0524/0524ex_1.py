'''
2023.05.24
박수연

# 문제정의
    - 난수를 발생시켜 num.txt 파일을 만들고, 이 파일을 이용해서 각 학생의 평균을 구한 다음 avg.txt 파일에 저장하기
'''

# num.txt 파일 만들기
import random
with open("c:/data/num.txt", 'w') as f: # 파일 객체 생성, with라 close 안해도 됨
    for i in range(5): # 줄 반복
        for i in range(5):  # 랜덤 수 찍기 반복
            f.write(str(random.randint(1,100))) # 줄 반복, 랜덤 수 찍기 반복을 파일에 쓰기, 1부터 100까지 숫자를 난수 발생시키고 문자열로 바꿔주기
            f.write(' ')    # 숫자 다음에 공백 넣기
        f.write('\n')   # 줄 바꿈 하기

# avg.txt 파일 만들기
with open("c:/data/num.txt", 'r') as f1:    # 파일 객체 생성, 읽기모드, 파일 변수 이름은 f1
    with open("c:/data/avg.txt", 'w') as f2:    # 파일 객체 생성, 쓰기모드, 파일 변수 이름은 f2

        j=0 # 학생 수
        while True: # 학생이 정확히 몇 명인지 모를 수 있으므로 무한반복
            j=j+1   # n번째 학생 5까지 반복시킴
            score=f1.readline()   # num.txt 파일 한줄 읽어오기
            if score=='':   # 읽어올 내용이 공백이라면 (더 이상 읽어올 내용이 없다면)
                break       # 반복 종료
            scorelist=score.split() # split(), 읽어 온 한 줄을 공백을 기준으로 리스트로 바꿔줌

            sum=0   # 합계 저장할 변수 0으로 초기화
            for i in range(5):  # 한 학생당 5과목의 점수 더하기, 5번 반복
                sum=sum+int(scorelist[i])    # scorelist의 i번째 값을 더함, 정수로 바꿔주기

            print("%d번 학생의 평균:"%j, sum/5, file=f2)   # 프린트 문으로 파일에 기록할 땐 *file=기록할 파일 변수 이름*
