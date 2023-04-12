'''
2023.04.12
박수연
입력받은 두 수의 크기를 비교

#문제 분석
    변수 - 숫자1 (num1), 숫자2 (num2)
 알고리즘
    1. 변수 선언
        num1, num2에 정수 입력
    2. 논리 (선택)
        if num1>num2:
            (참)큰 수 num1, 작은 수 num2
        else:
            (거짓)큰 수 num2, 작은 수 num1
'''

num1=int(input('첫 번째 숫자를 입력하세요 : ')) #입력 받은 숫자를 정수로 저장
num2=int(input('두 번째 숫자를 입력하세요 : ')) #입력 받은 숫자를 정수로 저장

if num1>num2:
    print('두 수 중에 큰 숫자는', num1,'이고, 작은 숫자는', num2)
else:
    print('두 수 중에 큰 숫자는', num2, '이고, 작은 숫자는', num1)


'''
if num1>num2:
    print('두 수 중에 큰 숫자는 {}이고, 작은 숫자는 {}'.format(num1,num2))
else:
    print('두 수 중에 큰 숫자는 {}이고, 작은 숫자는 {}'.format(num2,num1))
'''