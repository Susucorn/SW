'''
2023.05.16
박수연
파일 입출력 - seek(0) - 파일의 처음으로 포인트 이동
           - read(int n) - 지정한 갯수만큼 파일 읽어 오기
'''
f = open("C:/data/test.txt",'r')   #C:\data 경로의 폴더에 텍스트 파일에다 r 읽기 모드 (경로를 복붙하고 슬래시로 바꾸기) 

print(f.read(10), end='')   # 문자열 10개를 읽어오기, 출력
print(f.read(10), end='')
print(f.read(10))

f.seek(0) # 파일의 처음으로 포인터 이동

print(f.read(10), end='')   # 문자열 10개를 읽어오기, 출력
print(f.read(10), end='')
print(f.read(10))

f.close()   # 파일 닫기