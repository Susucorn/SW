'''
2023.04.19
박수연
두 정수를 입력받아 두 정수의 연산 값이 출력되는 프로그램 작성

#문제 분석
    번수 - x의 값 (x), y의 값 (y)
    조건 - y는 나눗셈의 몫을 계산할 때 0이 되면 안됨

#수식
    1. x > y 이면 x // y (y는 0이 되면 안됨)
    2. x < y 이면 x + y
    3. x == y 이면 x * y

#알고리즘
    1. 변수 선언 (x 와 y는 정수 값으로 입력받기)
    2. 논리연산 (if elif else)
    if x>y and y!=0 :
        x를 y로 나눈 값 출력
    elif x<y :
            x와 y의 합을 출력
    elif x==y :
            x와 y의 곱을 출력
    else:
        y의 값은 0입니다 출력
        
'''

x=int(input('x의 값을 입력하세요 : '))  #x의 값을 정수로 입력받기
y=int(input('y의 값을 입력하세요 : ')) #y의 값을 정수로 입력받기

if x>y and y!=0:
    print(x//y)
elif x<y:
    print(x+y)
elif x==y:
    print(x*y)
else:
    print('y의 값은 0 입니다.')