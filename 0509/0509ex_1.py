'''
2023.05.09
박수연
두 개의 숫자를 입력 받아서 두 수 사이의 합계 구하기

# 문제분석
    변수 - 첫 번째 정수 (num1), 두 번째 정수 (num2), 합계 저장할 변수 (sum), 값을 임시로 저장할 변수 (temp)
    조건 - 선택논리, 반복논리
# 알고리즘
    1. 변수 선언 (입력받는 값은 정수형, 변수 초기화)
        num1, num2는 정수를 입력받아 변수를 초기화
        sum=0, temp=0
    2. 조건
        1) 선택논리 (항상 num1이 num2보다 작거나 같을때)
            if num1이 num2보다 크다면
                num1과 num2의 값을 바꿈
        
        2) 반복논리 (num1부터 num2까지 1씩 증가하면서 더하기)
            while i가 num2보다 작거나 같다면 반복
                sum=sum+i (sum에 합계 저장)
'''

num1=int(input('첫 번째 숫자 입력 :'))  # 입력받는 값은 정수형
num2=int(input('두 번째 숫자 입력 :'))  # 입력받는 값은 정수형
sum=0   # 합계 변수 초기화
temp=0  # 변수 초기화

if num1>2:
    temp=num1   # num1 값을 temp 변수에 임시 저장
    num1=num2   # num2 값을 num1에 저장
    num2=temp   # temp 값을 num1에 저장

i=num1  # i를 num1로 초기화
while i<=num2:
    sum=sum+i
    i=i+1

print('{}~{}까지의 합계는 {}이다 .'.format(num1,num2,sum))
