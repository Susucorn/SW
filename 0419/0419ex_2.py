'''
2023.04.19
박수연
입력된 수가 양수,0,음수인지 판별하는 프로그램 작성

#문제분석
    변수 - 숫자 (num)
    수식 - num > 0 이면 양수, num < 0 이면 음수
#알고리즘
    1. 변수 선언
        num 에 정수로 입력받기
    2. 논리 (선택)
        if num>0:
            양수 출력
        if num<0
            음수 출력
        if num==0
            0 출력

#알고리즘
    1. 변수 선언
        num 에 정수로 입력받기
    2. 논리 (선택)
        if num>0:
            양수 출력
        elif num<0:
            음수 출력
        else:
            0 출력
'''

#단순 if
num=int(input('숫자 입력 : ')) #입력받은 값은 정수

if num>0:
    print('입력한 값',num,'은 양수입니다.')
if num<0:
    print('입력한 값',num,'은 음수입니다.')
if num==0:
    print('입력한 값',num,'은 0입니다.')

#다중 if
num=int(input('숫자 입력 : ')) #입력받은 값은 정수

if num>0:
    print('입력한 값',num,'은 양수입니다.')
elif num<0:
    print('입력한 값',num,'은 음수입니다.')
else:
    print('입력한 값',num,'은 0입니다.')
