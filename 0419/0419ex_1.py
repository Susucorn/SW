'''
2023.04.19
박수연
성별, 키, 몸무게를 입력받아 비만도 측정하는 프로그램 작성

#문제분석
    변수 - 성별 (sex), 키 (height), 몸무게 (weight), 평균체중(avg)
    수식 - (남자일때 : avg=height*height*22) (여자일때 : avg=height*height*21)
            (bmi : weight/avg*100)

#알고리즘
    1. 변수 선언하기
    2. 키, 몸무게, 성별을 입력받기 (키, 몸무게는 실수로 입력받기)
    3. 논리(선택 - 내포된 선택(선택문 안에 또 다른 선택문))
        if 성별이 여자:
            avg 계산하고
            if bmi>=120:
                과체중 출력
            elif 110<=bmi<=119
                비만체중 출력
            else
                표준 체중 출력
        elif 성별이 남자:
            #알고리즘 똑같으니 생략
        else:
            성별 잘못 입력 출력

'''

sex=input('성별 입력("M or m")또는 ("F or f") : ') # 성별 입력받기
height=float(input('키 입력(cm) : '))/100 # 키는 실수로 입력받기, 입력받은 값을 100으로 나누어 m로 단위 변환
weight=float(input('몸무게 입력(kg) : '))/100 # 몸무게는 실수로 입력받기, 입력받은 값을 100으로 나누어 m로 단위 변환

if (sex=='M' or sex=='m'): #남자
    avg=height*height*22 #표준체중
    bmi=weight/avg*100
    if 110<=bmi<=119:
        print('과체중')
    elif bmi>=120:
        print('비만 체중')
    else:
        print('표준체중')

elif (sex=='F' or sex=='f'): #여자
    avg=height*height*21 #표준체중
    bmi=weight/avg*100
    if 110<=bmi<=119:
        print('과체중')
    elif bmi>=120:
        print('비만 체중')
    else:
        print('표준체중')

else:
    print('성별 입력이 잘못 되었습니다.')