'''
파이썬 기초-자료형
2023-03-22
박수연
'''

a=100 #10진수 정수
b=0b1100100 #2진수 정수
c=0o144 #8진수 정수

print('변수 a의 값은:',a,'이고 자료형은',type(a))
print('변수 b의 값은:',b,'이고 자료형은',type(b))
print('변수 c의 값은:',c,'이고 자료형은',type(c))

a1=100.0 #소수점을 가진 실수
b1=0.1e3 #e를 이용한 실수 0.1*10^3
c1=100000E-2 #대문자E를 이용한 실수 100000*10^-2
print() #한줄 띄우기
print('변수 a1의 값은:',a1,'이고 자료형은',type(a1))
print('변수 b2의 값은:',b1,'이고 자료형은',type(b1))
print('변수 c3의 값은:',c1,'이고 자료형은',type(c1))