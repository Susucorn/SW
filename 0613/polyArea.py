'''
2023.06.13
박수연

모듈 생성하기
'''

pi = 3.14159

def rectangleArea(width, depth):    # 사각형의 넓이를 계산하는 함수
    return width * depth

def triangleArea(base, height):     # 삼각형의 넓이를 계산하는 함수
    return base * height / 2

def circleArea(r):                  # 원의 넓이를 계산하는 함수
    return pi * r * r


def circumference(r):               # 원의 둘레를 계산하는 함수
    return 2 * pi * r