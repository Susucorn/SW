'''
2023.04.11
박수연
선택문 - if, if~else
(1) 입력받은 성적이 80점 이상이면 '합격입니다.' 출력
        그리고 성적과 상관없이 '수고했습니다.' 출력

(2) 성적이 80 이상이면 '합격입니다.' 출력
        성적이 80 미만이면 '불합격입니다.' 출력
    성적과 관계없이 '수고하셨습니다.' 출력
'''

#단순 if
score=int(input('점수를 입력하세요 : ')) # 키보드로 입력받은 변수는 score에 저장함
if score>=80: #선택 조건
    print('합격 입니다.') #조건이 참일 때만 실행되는 문장

print('수고하셨습니다.') #조건과 관계없이 항상 실행되는 문장

#if~else
jumsu=int(input('점수를 입력하세요 : '))
if jumsu>=80: #선택 조건
    print('합격입니다.') #조건이 참일 때만 실행되는 문장
else:
    print('불합격입니다.') #조건이 거짓일 때만 실행되는 문장

print('수고하셨습니다.') # 조건과 관계없이 항상 실행되는 문장