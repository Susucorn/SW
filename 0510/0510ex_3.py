'''
2023.05.10
박수연
사용자로부터 하나의 숫자를 입력받아 *을 출력하는 프로그램

# 문제분석
    변수 - 입력받을 숫자 (num)
    논리 - 반복논리 (for)
# 알고리즘
    1. 변수 초기화 (입력받는 값은 정수형)
            입력받은 숫자로 변수 초기화
    2. 중첩반복 
            for i in range(1,num+1)  - 줄 반복
                for j in range(1,i+1)   - 별 찍기 반복
                    별찍기
'''
num=int(input('숫자 입력 : '))

for i in range(1,num+1):        # 줄 반복
    for j in range(1,i+1):      # 별 찍기 반복
        print('*', end="")      # 별 출력, 옆으로 공백없이
    print() # 줄 바꿈


# 거꾸로 출력
print("\n거꾸로 출력")

num=int(input('숫자 입력 : '))

for i in range(num,0,-1):       # 줄 반복
    for j in range(i,0,-1):     # 별 찍기 반복
        print('*', end="")      # 별 출력, 옆으로 공백없이
    print() # 줄 바꿈
