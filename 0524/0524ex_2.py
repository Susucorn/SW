'''
2023.05.24
박수연

# 문제정의
    score1.txt 파일을 읽어와서 각 학생의 등급을 결정하고 결과를 report1.txt 파일에 저장하기
'''

score=[]    # 리스트 변수 생성, 아직 값은 없음
f=open("c:/data/score1.txt", 'r')   # 읽기 파일 객체 생성

for i in range(10): # 10명의 학생 점수 읽어오기
    score.append(f.readline().split())  # 괄호 안의 내용을 score에 append(추가) 하기, 파일(f)의 내용을 한줄씩 읽어와서(readline) 공백을 기준으로 하나씩 나누어서(split) score 리스트에 저장하기

for j in range(10): # 10명의 학생 등급 매기기를 10번 반복하기
    score[j][1]=float(score[j][1])  # 문자열을 실수로 변환, 리스트는 문자열로 저장하기 때문

    if score [j][1]>=90:        # 점수가 90 이상이면
        score[j].append("A")    # score의 j 부분에 A 추가하기
    elif score [j][1]>=80:      # 점수가 80 이상이면
        score[j].append("B")    # score의 j 부분에 B 추가하기
    elif score [j][1]>=70:      # 점수가 70 이상이면
        score[j].append("C")    # score의 j 부분에 C 추가하기
    else:
        score[j].append("D")

for i in range(10): #10명의 등급을 화면에 출력
    print("{:<5}{:<5}".format(score[i][0],score[i][2]))

f.close

'''
한글이 읽히지 않아 영어로 바꾸기
'''