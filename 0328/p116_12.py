'''
2023.03.28
박수연
윗변 23cm, 아랫변 34cm, 높이 13cm인 사다리꼴의 넓이를 구하기
변수 : 윗변, 아랫변, 높이, 사다리꼴 넓이
수식 : 사다리꼴 넓이 = ((윗변 + 아랫변) * 높이)/2
알고리즘 : 변수 선언, 사다리꼴 넓이 구하기, 결과 출력
'''

t=23
b=34
h=13
area=0

area=(t+b)*h/2
print('윗변이', t,'cm, 아랫변이', b, 'cm, 높이가', h, 'cm인 사다리꼴의 넑이는 :', area)