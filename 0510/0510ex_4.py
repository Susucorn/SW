'''
2023.05.10
박수연
3의 배수를 더해 입력받은 숫자가 3의 배수의 총합을 넘었을 때 N값과 총합계, N 값이 몇 번째 인지 while 반복문을 사용한 프로그램 작성

# 문제 분석
    변수 - 입력받을 값 (num), 합계 초기화 변수 (sum), 3의 배수의 갯수 (count)
    논리 - 반복조건 (while)

# 알고리즘
    1. 변수 초기화 (입력받은 값은 정수형)
        합계와 갯수 변수 초기화
    2. 반복논리
        while True:
            i는 3의 배수여야하므로 i+3
            3의 배수 합계 저장
            횟수 1씩 증가
        선택논리
            if sum이 num보다 크다면
                반복 종료
    3. 결과 출력
'''

num=int(input('사용자 입력 : '))
sum=0
count=0
i=0

while True:
    i=i+3
    sum=sum+i
    count=count+1
    if sum>num:
        break
print('')
print('')
print('')