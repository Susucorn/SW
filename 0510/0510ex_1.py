'''
2023.05.10
박수연
입력받은 숫자가 소수인지 여부를 출력하는 프로그램

# 문제분석
    변수 - 입력받는 숫자 (num)
    논리 - 반복논리 (for), 선택논리 (if)    - 반복문 안에 선택문 포함

# 알고리즘
    1. 변수 초기화(입력받은 값은 정수형)
    2. 반복논리
            for i in range(2,num+1)
                if num을 i로 나눈 나머지가 0이라면
                    반복멈춤
            
            if num이 i와 같다면
                소수입니다 출력
            else
                소수가 아닙니다 출력
            
            소수 판별 프로그램을 이용해주셔서 감사합니다 출력
'''

num=int(input('소수 검증 숫자 입력 : '))    # 입력받는 정수로 변수 초기화

for i in range(2,num+1):    # 1은 모든 값에 포함되므로 2부터 시작하여 num+1까지, 뒤에 1씩 증가는 생략가능
    if num%i==0:
        break   # 반복 종료

if num==i:      # num을 i로 나눴을때 나머지가 0이 되려면 두 개의 값이 똑같아야함
    print('소수 입니다.')
else:
    print('소수가 아닙니다.')

print('소수 판별 프로그램으 이용해주셔서 감사합니다.')