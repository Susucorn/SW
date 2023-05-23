'''
2023.05.16
박수연
파일 입출력 - writlinee() - 리스트나 튜플 같은 자료형을 파일에 저장 (저장된 데이터는 반드시 문자열이여야 함)
            - write() - 문자열만 파일에 출력
'''

L1 = ["충청남도", "충청북도\n", "전라남도", "전라북도\n", "경상남도", "경상북도"]   # 문자열 리스트 자료형를 L1에 저장
L2 = [1,2,3,4,5]    # 정수형 리스트 자료형을 L2에 저장

with open("C:/data/test.txt", 'w') as f: # with 구문으로 파일 객체 생성
    f.writelines(L1)    # L1 리스트 자료형 내용을 파일에 출력, L2는 정수형 리스트이기 때문에 오류