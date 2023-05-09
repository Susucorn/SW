'''
2023.05.09
박수연
1부터 1000까지의 정수 중 입력받은 숫자의 배수만 더하기

# 문제분석
    변수 - 입력받는 정수 (num), 합계 저장 변수 (total)
    조건 - 반복논리(for)
# 알고리즘
    1. 변수 초기화
            num 변수에 정수를 입력받아 변수 초기화
            total 변수 0으로 초기화
    2. 반복논리 (for)
        for i in range(num,1001,num)
            합계 저장
'''

num=int(input('합을 원하는 배수 입력 : '))
total=0

for i in range(num,1001,num):
    total=total+i

print('1부터 1000까지의 {}의 배수의 합은 : {}'.format(num,total))