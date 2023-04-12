'''
2023.04.12
박수연
두 정수를 정수로 입력 받은 후 모두 짝수이면 "모두 짝수", 
홀수이면 "모두 홀수", 
그렇지 않으면 "홀수 , 짝수 섞여있음" 출력하기

#문제 분석
    변수 - 숫자1 (num1), 숫자2 (num2)
    수식 - num1%2==0 and num2%2==0 (짝수)
            num1%2!=0 and num2%2!=0 (홀수)
 알고리즘
    1. num1, num2에 정수 입력 받기
    2. 논리 (선택) - if~elif~else
        if num1%2==0 and num2%==0:
            (조건 1 참) "모두 짝수"
        elif num1%2==1 and num2%==1:
            (조건 2 참) "모두 홀수"
        else:
            (거짓) "홀수 짝수 섞여있음"

'''

num1=int(input('첫 번째 숫자를 입력하세요 :'))
num2=int(input('두 번째 숫자를 입력하세요 :'))

if num1%2==0 and num2%2==0:
    print('두 숫자는 모두 짝수 입니다.')
elif num1%2==1 and num2%2==1:
    print('두 숫자는 모두 홀수 입니다.')
else:
    print('짝수와 홀수가 섞여 있습니다.')