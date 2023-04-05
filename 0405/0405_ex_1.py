'''
2023.04.05
박수연
표준입력(input()) 연습
'''

num1=float(input('실수 입력 : ')) #첫 번째 실수
num2=float(input('실수 입력 : ')) #두 번째 실수

print('num1+num2=', num1+num2)

tup1=eval(input('(1,2,...)형태의 튜플 데이터 입력 : '))
print('튜플 자료 :', tup1, type(tup1))

lst1=eval(input('[1,2,...]형태의 리스트 데이터 입력 : '))
print('리스트 자료 : ',lst1,type(lst1))