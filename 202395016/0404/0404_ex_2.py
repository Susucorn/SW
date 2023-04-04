'''
2023.04.04
박수연
표준출력(print) format()연습
'''

print('이름은 {}이고 나이는 {}입니다.'.format('박수연', 21))
print('이름 {name}, 나이 {age}, 주소 {add}'.format(add='김해', name='박수연', age=21)) #중괄호가 있다는 건  포맷메소드를 썼다는 뜻
print('The lucky number is ({:14})'.format(7777)) #숫자는 기본적으로 오른쪽 정렬
print('The lucky number is ({:<14})'.format(7777)) #숫자 왼쪽 정렬