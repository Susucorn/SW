'''
2023.04.12
박수연
평점을 입력받아 평점 출력, 4.2 이상이면 "해외연수 기회 부여" 출력

#문제 분석
    변수 - 평점(score)
 알고리즘
    1. 변수 선언
        score에 평점은 실수로 입력 받기
    2. 논리(선택)
        if score>=4.2:
'''

score=float(input('enter your score : ')) #학점을 실수로 입력 받기
print('당신의 평점은 : ', score)

if score>=4.2:
    print('해외 연수 기회 부여') #조건이 참일 때만 실행됨
