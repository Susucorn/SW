'''
2023.06.07
박수연

# 문제정의
    랜덤으로 2개의 set 만든 후 합집합, 교집합, 차집합 구하는 프로그램

# 문제분석
    변수 - 랜덤으로 만들어지는 세트 변수 저장할 값 (num1, num2)
# 알고리즘
    1. 랜덤 모듈 추가
    2. 비어있는 세트 변수 2개 생성
    3. 반복 (무한반복 - 갯수가 10개가 될때 까지 반복)
        3-1. 조건문 (if - len의 길이가 10개보다 작다면)
            num1 = 랜덤 수 추가
        3-2. 조건문 (if - len의 길이가 10개보다 작다면)
            num2 = 랜덤 수 추가
    4. 합집합, 교집합, 차집합        
'''

import random   # 랜덤 모듈 추가
num1=set()
num2=set()      # 세트는 무조건 set() 함수로 써야함

while True:                                 # 무한반복, 세트는 값의 중복을 허용하지 않기 때문에 무한반복하여 10개의 숫자를 생성
    if len(num1)<10:                        # num1의 길이가 10보다 작다면
        num1.add(random.randint(1,100))     # 1부터 100사이의 랜덤 수 추가

    if len(num2)<10:                        # num2의 길이가 10보다 작다면
        num2.add(random.randint(1,100))     # 1부터 100사이의 랜덤 수 추가

    if len(num1)==10 and len(num2)==10:     # num1 과 num2 의 원소가 10개라면 무한반복 종료
        break

print("발생한 10개의 난수 num1 :",num1)
print("발생한 10개의 난수 num2 :",num2)
print('합집합 :',num1|num2)
print('교집합 :',num1&num2)
print('차집합 :',num1-num2)