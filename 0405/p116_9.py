'''
2023.04.05
박수연
월급 수령액을 구하는 프로그램 작성하기
'''

sal=int(input('홍길동의 본봉은 :')) #본봉 변수 값 받기
pay=int(input('이번 달 수당은 :')) #수당 변수 값 받기

tax=(sal+pay)*0.2 #세금 구하기
print('홍길동의 본봉은 {}이고, 월급 수령액은{}이다.'.format(sal,sal+pay-tax))