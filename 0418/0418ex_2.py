'''
2023.04.18
박수연
두 과목 모두 75이상 총점 180이상이면 '최우수학생', 총점이 160 이상이면 '우수학생', 총점이 150 이상이면 '보통학생', 두 과목 점수 모두가 75점 이상이 아니면 '분발합시다'출력

#문제분석
    변수 - 과목 점수 1 (score1), 과목 점수 2 (score2), 두 과목 합계 (total)
#알고리즘
    1. 변수 선언하기
    2. if score1>=75 and score2>=75:
    if total>=180:
        print('최우수학생')
    elif total>=160:
        print('우수학생')
    else:
        print('보통학생')
print('분발하세요')
'''

score1=int(input('성적1을 입력하세요 :')) # 성적1를 정수로 받기
score2=int(input('성적2을 입력하세요 :')) # 성적2를 정수로 받기
total=score1+score2

if score1>=75 and score2>=75: #조건 1
    if total>=180: #조건 2
        print('최우수학생') #조건 1과 2가 참일 때 출력
    elif total>=160: #조건 3
        print('우수학생') #조건 1은 참, 조건 2가 거짓이고 조건 3이 참일 때 출력
    else:
        print('보통학생') #조건 1은 참, 2와 3은 거짓일때 출력
else:
    print('분발하세요')

