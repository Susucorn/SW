'''
2023.05.16
박수연
파일 입출력 - r 읽기 read() - 전체 내용을 하나의 문자열로 반환
'''

f = open("C:/data/test.txt",'r')    #C:\data 경로의 폴더에 텍스트 파일에다 r 읽기 모드 (경로를 복붙하고 슬래시로 바꾸기)

txts = f.read() # 파일의 전체 내용을 txts 변수에 하나의 문자열로 반환   (read는 전체 내용을 읽고 출력되기 때문에 반복문 필요 X)

print(txts) # read로 읽어 내용을 화면에 출력

f.close()   # 파일 닫기

