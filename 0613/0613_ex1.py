'''
2023.06.13
박수연

# 문제정의
    3개의 숫자를 입력받아 가장 큰 수를 구하는 프로그램
    findmax(a, b, c)함수로 작성하기

# 알고리즘
    1. findmax() 함수 선언 (함수를 먼저 정의 해야함)
        1-1. a, b, c중 가장 큰 값 찾기
    2. 정수로 숫자 입력받기 (num1, num2, num3)
    3. 입력받은 findmax(num1, num2, num3) 호출
    4. return 받은 가장 큰 값 출력
'''

# 가장 큰 값 찾기
def findmax(a, b, c):   # findmax 라는 이름의 변수를 선언, 매개변수는 a, b, c
    if a > b :          # a가 b보다 크다면
        biggest = a     # 제일 큰 수는 a
    else:
        biggest = b     # 그렇지 않다면, 제일 큰 수는 b
    
    if biggest < c :    # biggest에 있는 값이 c 보다 작다면
        biggest = c     # 제일 큰 수는 c

    return biggest      # 가장 큰 값을 반환

# 값을 입력받기
num1 = int(input("첫 번째 숫자 입력 : "))
num2 = int(input("두 번째 숫자 입력 : "))
num3 = int(input("세 번째 숫자 입력 : "))    # 정수로 입력받기 num1, num2, num3 변수에 저장

# 함수를 호출하고 return문에 의해 반환되는 값을 biggest_number 변수에 저장하기
biggest_number = findmax(num1, num2, num3)                  # 함수 호출, return된 값 변수에 저장
print("세 개의 숫자 중에 가장 큰 숫자는 : ", biggest_number)  # 가장 큰 값 출력
