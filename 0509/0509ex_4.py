'''
2023.05.09
박수연
1부터 100까지의 정수 중 입력받은 숫자의 배수만 더하기

# 문제분석
    변수 - 입력받는 숫자 (num), 합계를 저장할 변수 (total), 초기화 변수 (i)
    조건 - 반복논리 (while, continue), 선택논리(if)
# 알고리즘
    1. 변수 초기화
            num은 입력받은 숫자로 초기화
            i는 0으로 초기화
            total은 0으로 초기화
    2. 반복논리 (while)
        while i가 100보다 작거나 같다면 반복
            i를 1씩 증가시킴
       선택논리 (if)
            if i를 num으로 나눈 나머지가 0이 아니라면
                continue (반복문 처음으로 다시 돌아가게 함)
            반복문이 참이라면 total변수에 합계 저장
'''

num=int(input('배수 숫자 입력 : ')) # 입력받은 값은 정수
i=0
total=0

while i<=100:
    i=i+1
    if i%num!=0:
        continue    # 반복문의 처음으로 이동, 참이 되면 다음 문장 실행
    total=total+i   # 반복문이 참이 되면 합계를 저장

print('1부터 100까지의 {}의 배수의 합은 : {}'.format(num,total))