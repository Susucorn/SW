'''
2023.05.03
박수연

#문제정의
    1~ 입력받은 숫자까지의 합계 구하기
#문제분석
    변수 - 입력받을 숫자 (num), 합계 (total)
#알고리즘
    1. 변수 지정하기 (입력받는 숫자는 정수형)
    2. 합계 초기화 (total)
    3. 반복문
        for i in range(1,num+1):
            total=total+i
        합계 출력

        while i<=num:
            total=total+i
            i=i+1
        합계 출력
'''

# for 반복
num=int(input('숫자 입력 : '))
total=0
for i in range(1,num+1):
    total=total+i
print("1~{}까지의 합계는 : {}".format(num,total))

# while 반복
num=int(input('숫자 입력 : '))
i=1
total=0
while i<=num:
    total=total+i
    i=i+1
print("1~{}까지의 합계는 : {}".format(num,total))