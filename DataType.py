import math
import random
import statistics
import pandas

# 숫자형
print(1.1)          # float
print('1+1', 1+1)   # 문자, int
print(math.sqrt(4))
print(math.pow(4, 2))
print(random.random())

# 문자형
print(len('hello world'))
print('''
hello
world
''')                        # 자유로운 문장 쓰기
print("'1'+'1'", '1'+'1')   # 통짜 문장과 결합 연산자
print('hello' * 10)         # 반복
print('hello world'.replace('world', 'univ'))

# 리스트형
students = ["A", "B", "C"]
grades = [2, 1, 4]
print(students[0])
print(len(students))        # 원소 개수
print(min(grades))
print(max(grades))
print(sum(grades))
print(statistics.mean(grades))      # 평균
print(random.choice(students))      # 무작위 출력

# 변수
price = 10000
shit = 0.1
print(price * shit)

name = input('name : ')                 # 입력 받기
print('hi ' + name + ' bye ' + name)

# 디버깅 : 반 잘라서 후보 좁히기, 절반 쯤에 print문 사용해 출력문에 문제 생기는지 파악

# pypi로 데이터 추출
house = pandas.read_csv('house.csv')
print(house)
print(house.head(2))
print(house.describe())

# 조건문
input_id = input('id : ')
id1 = 'aaa'
id2 = 'xxx'
if (input_id == id1):
    print('welcome')
elif (input_id == id2):
    print('???')
else:
    print('bye')

# 반복문 : 리스트 요구 -> 이름 없이 데이터에 순서 줄 때
names = ['asd', 'zxc', 'qwe']
for man in names:
    print('hi '+man+' bye '+man+'.')

persons = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
print(persons[0][0])        # 개별에 이름 부여 가능
for mans in persons:
    print(mans[0]+', '+mans[1]+', '+mans[2])

# 사전형(딕셔너리) : 값의 이름(키) + 값(value) -> 순서 상관 없이 데이터에 이름 줄 때
dic_person = {'name':'ego', 'address':'seoul', 'interest':'web'}
print(dic_person['name'])

for key in dic_person:
    print(key, dic_person[key])

dic_persons = [
    {'name':'ego1', 'address':'seoul', 'interest':'web'},
    {'name':'ego2', 'address':'seoul', 'interest':'web'},
    {'name':'ego3', 'address':'seoul', 'interest':'web'}
]

for person in dic_persons:
    for key in person:
        print(key, ':', person[key])
    print('---------')