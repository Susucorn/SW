'''
2023.05.23
박수연

# 문제정의
    키보드로 입력받은 내용을 리스트에 저장하고 파일에 저장하기

# 문제분석
    변수 - 입력값 저장할 리스트 (enter), 키보f 입력받은 내용 저장 (txt)

# 알고리즘
    1. 변수 초기화
        enter=[]
    2. 파일 객체 생성 - 쓰기모드
    3. 파일 처리
        1) 반복 (while True: )
            txt=문장입력받기
            선택 (if txt=='' :) 입력받는 값ㅇ리 아무것도 없다면
                반복 멈춤
            text를 enter(리스틑 변수)추가
        2) 파일에 결과 출력 
    4. 파일 닫기
'''

enter=[]    # 리스트 변수로 선언

f=open("c:/data/out.txt",'w')   # 파일 객체 생성 , 쓰기 모드

while True:
    text=input('문장입력(끝:엔터키): ') # 문자열 입력
    if text=='': # 입력 내용이 없다면
        break    # 반복 종료

    enter.append(text+'\n')  # 입력받은 내용을 리스트에 추가함, 한 문장 입력받을때마다 줄 바꿈

f.writelines(enter)    # 리스트이기 때문에 writelines, 리스트 자료형을 파일에 출력
f.close()              # 파일 닫기

print("입력될 리스트", enter)
print("out.txt파일이 생성되었습니다.")