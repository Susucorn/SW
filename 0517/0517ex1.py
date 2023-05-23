'''
2023-05-17
박수연
파일 입출력
'''

#for 반복문으로 파일 읽어오기
with open("C:/data/linetest.txt","r") as f : #파일 열기
    for line in f : #파일 객체를 지정해서 반복문 작성
        print(line,end='') #줄 바꿈 없이 출력

#readline() : (한 줄씩 읽어 오기) 메소드로 파일 읽어 오기
print()

with open("C:/data/linetest.txt","r") as f : #파일 열기
    while True : #무한 반복
        line = f.readline() #파일 한 줄씩 읽어 오기
        print(line,end='') #줄 바꿈 없이 출력

        if line == '' : #읽어 올 내용이 없다면
            break #반복 종료

#readlines() : 한 줄씩 읽어서 리스트형으로 반환
print()

with open("C:/data/linetest.txt","r") as f : #파일 열기
    textlists = f.readlines() #한 줄씩 리스트 형식으로 읽어 오기
    print(type(textlists)) #변수 타임 확인
    print(textlists)

#print() 함수로 파일에 출력하기
print()

f = open("C:/data/ptest.txt","w") #쓰기 모드의 파일 객체 생성

print("aaaaaaa",file=f) #파일에 출력
print("bbbbbbb",file=f) #파일에 출력
print("ccccccc",file=f) #파일에 출력

f.close() #파일 닫기