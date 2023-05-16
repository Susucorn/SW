'''
2023.05.16
박수연
파일 입출력 - w 쓰기
'''
f = open("C:/data/test.txt", 'w') #C:\data 경로의 폴더에 텍스트 파일을 만들고 쓰기 모드 (경로를 복붙하고 슬래시로 바꾸기)

for i in range(1,11):   # 10번 반복
    f.write("%d번째 줄입니다.\n"%i)    # f에 i 출력

f.close()   # 파일 종료
