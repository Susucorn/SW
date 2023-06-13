'''
2023.06.13
박수연

# 문제정의
    하나의 숫자를 입력받아 1부터 입력된 숫자 사이의 약수를 출력하는 프로그램
    dNumber()함수로 작성하기

# 알고리즘
    1. dNumber() 함수 선언
        1-1. 약수 구하기
    2. 정수로 숫자 입력받기(num)
    3. 약수를 저장할 list 변수 선언(num_list)
    4. dNumber() 호출
    5. 약수가 저장된 list 출력
'''

# 약수 구하기
def dNumber(num, num_list):          # dNumber 함수 선언
    for i in range(1,num+1):         # 1부터 num까지 순차적으로 반복
        if num%i==0:                 # 약수인 조건, num을 i로 나눈 나머지가 0이라면
            num_list.append(i)       # num_list에 i를 추가하기

# 값을 입력받기
num = int(input("자연수 입력 : "))    # 정수로 입력받기
num_list = []                        # 빈 리스트 변수 선언

# 함수를 호출하여 출력하는 조건
if num > 0:                          # num이 0보다 크다면
    dNumber(num, num_list)           # dNumber()함수 호출
    print(num, "의 약수는 : ", num_list)
else:
    print("자연수가 아닙니다.")
