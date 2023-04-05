'''
2023.04.05
박수연
5과목 점수 입력 받아서 합계 구하는 프로그램 작성하기 (p114 - 14번)
'''

sub1=int(input('과목1의 점수는 :')) #과목 1 점수 입력받기
sub2=int(input('과목2의 점수는 :')) #과목 2 점수 입력받기
sub3=int(input('과목3의 점수는 :')) #과목 3 점수 입력받기
sub4=int(input('과목4의 점수는 :')) #과목 4 점수 입력받기
sub5=int(input('과목5의 점수는 :')) #과목 5 점수 입력받기

total=sub1+sub2+sub3+sub4+sub5 #합계 구하기
avg=total/5 #평균 구하기
print('5과목의 합계는 {}이고, 평균은 {}이다.'.format(total, avg))


