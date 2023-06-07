'''
2023.06.07
박수연

# 문제정의
    5명 학생의 학번, 전화번호를 입력받아 딕셔너리에 저장, 학번으로 전화번호 검색하여 출력하는 프로그램

# 문제분석
    변수 - 학번 (id), 전화번호부 (phone), 전화번호 (phone_n)
# 알고리즘
    1. 전화번호 변수 생성 (딕셔너리)
    2. 반복문 - 5번 반복하기
        id 변수에 학번 저장
        phone_n 변수에 전화번호 저장
    3. 조건문 (if ~ else) - 내가 입력한 id(학번)가 phone 딕셔너리에 있다면 (id in phone)
        학번에 해당하는 전화번호 출력
        그렇지 않다면 전화번호가 존재하지 않다는 메세지 출력하기
'''

phone={}            # 전화번호 딕셔너리 생성

for i in range(5):  # 5번 반복
    id=int(input(str(i+1) + ("번째 학생 학번 입력 : ")))          # i+1을 문자열로 바꾸어 문자열과 연결하기
    phone_n=input(str(i+1) +("번째 학생 전화번호 : "))          # 전화번호를 입력받을때 문자로 받기

    phone[id]=phone_n                                          # 학번, 전화번호를 전화번호부 딕셔너리에 추가

print("학생 전화번호부가 완성되었습니다.")

id=int(input("검색을 원하는 학번 입력 : "))
if id in phone:                                   # 검색한 id 안에 phone이 있다면
    print("입력한 학생의 전화번호 : "+phone[id])    # 학번에 해당하는 전화번호 출력
else:
    print("입력한 학생의 전화번호가 없습니다.")      # 전화번호가 없는 경우에 출력되는 문장