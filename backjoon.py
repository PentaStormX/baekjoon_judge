# 두 수 비교하기
"""
A, B = input().split()
A = int(A)
B = int(B)

if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")
"""

# 시험 성적
"""
def ConvertScore(score):
    if score >= 90 and score <= 100:
        print("A")
    elif score >=80 and score < 90:
        print("B")
    elif score >=70 and score < 80:
        print("C")
    elif score >=60 and score < 70:
        print("D")
    else:
        print("F")

N = int(input())
ConvertScore(N)
"""

# 윤년
"""
def CheckYoonYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(1)
    else:
        print(0)

y = int(input())
CheckYoonYear(y)
"""

# 사분면
"""
def SelectQuadrant(x,y):
    if x > 0 and y > 0:
        print(1)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    elif x > 0 and y < 0:
        print(4)

X = int(input())
Y = int(input())
SelectQuadrant(X, Y)
"""

# 알람 시계
"""
MINUTE = 60
MINUSTIME = 45

H, M = input().split()
H = int(H)
M = int(M)

if H == 0:
    H = 24
time = (((H * MINUTE) + M) - MINUSTIME) // 60
minute = (((H * MINUTE) + M) - MINUSTIME) % 60

if time == 24:
    time = 0

print(time, minute)
"""

# A+B - 7
"""
T = int(input())
list = []

for i in range(T):
    A, B = input().split()
    list.append(int(A)+int(B))

for i in range(T):
    print(f"Case #{i+1}: {list[i]}")
"""

# A+B - 8
"""
T = int(input())
total = []
first = []
second = []

for i in range(T):
    A, B = input().split()
    first.append(int(A))
    second.append(int(B))
    total.append(int(A)+int(B))

for i in range(T):
    print(f"Case #{i+1}: {first[i]} + {second[i]} = {total[i]}")
"""

# 별 찍기 - 1
"""
def printstar(n):
    for _ in range(n):
        print("*", end='')
    print("")

N = int(input())
for i in range(1, N+1):
    printstar(i)
"""

# 별 찍기 - 2
"""
def printstar(n):
    for _ in range(n):
        print("*", end='')
    print("")

def printspace(n):
    for _ in range(n):
        print(" ", end='')

N = int(input())
for i in range(1, N+1):
    printspace(N-i)
    printstar(i)
"""

# A+B - 4
"""
import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().rstrip().split())
        print(A+B)
    except :
        break
"""


# A+B - 5
"""
import sys

while True:
    A, B = map(int, sysno.stdin.readline().rstrip().split())
    if A == 0 and B == 0:
        break
    else:
        print(A+B)
"""

# 공 넣기
"""
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
dic = {}
for i in range(1, N+1):
    dic[i] = 0

for _ in range(M):
    i,j,k = map(int, sys.stdin.readline().rstrip().split())
    for j in range(i, j+1):
        dic[j] = k

for i in dic.keys():
    print(dic[i], end=" ")
"""

# 공 바꾸기
"""
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
dic = {}
for i in range(1, N+1):
    dic[i] = i

for _ in range(M):
    i,j = map(int, sys.stdin.readline().rstrip().split())
    temp = dic[i]
    dic[i] = dic[j]
    dic[j] = temp

for i in dic.keys():
    print(dic[i], end=" ")
"""

# 과제 안내신분~
"""
import sys
student = []
COUNT = 28

for _ in range(COUNT):
    student.append(int(sys.stdin.readline().rstrip()))

for i in range(1, 31):
    if student.count(i) == 0:
        print(i)
"""

# 나머지
"""
import sys
DIVIDE = 42
numlist = []

for _ in range(10):
    n = int(sys.stdin.readline().rstrip())
    if numlist.count(int(n % DIVIDE)) == 0:
        numlist.append(int(n % DIVIDE))

print(len(numlist))
"""

# 바구니 뒤집기
"""
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
dic = {}

for i in range(1, N+1):
    dic[i] = i


for _ in range(M):
    temp = []
    i, j = map(int, sys.stdin.readline().rstrip().split())
    for a in range(i, j+1):
        temp.append(dic[a])
    temp.reverse()
    cnt = 0
    for b in range(i, j+1):
        dic[b] = temp[cnt]
        cnt+=1

for i in dic.keys():
    print(dic[i], end=" ")
"""

# 평균
"""
import sys

N = int(sys.stdin.readline().rstrip())
scores = list(map(int, sys.stdin.readline().rstrip().split()))
M = max(scores)

total = 0
for i in scores:
    total += i / M * 100

print(total/len(scores))
"""

# 문자와 문자열
"""
import sys
S = sys.stdin.readline().rstrip()
i = int(sys.stdin.readline().rstrip())
print(S[i-1])
"""

# 단어 길이 재기
"""
import sys

E = sys.stdin.readline().rstrip()
print(len(E))
"""

# 문자열
"""
import sys
T = int(sys.stdin.readline().rstrip())
list = []

for _ in range(T):
    S = sys.stdin.readline().rstrip()
    list.append(S[0] + S[-1])

for a in list:
    print(a)
"""

# 아스키코드
"""
import sys

A = sys.stdin.readline().rstrip()
print(ord(A)) # 문자/숫자를 아스키코드로 변환 : ord()
"""

# 숫자의 합
"""
import sys
N = int(sys.stdin.readline().rstrip())
value = sys.stdin.readline().rstrip()
total = 0

for i in value:
    total += int(i)

print(total)
"""

# 알파벳 찾기
"""
import sys
S = sys.stdin.readline().rstrip()

eng = "abcdefghijklmnopqrstuvwxyz"
list = []

for i in eng:
    list.append(S.find(i))

for i in list:
    print(i, end=' ')
"""

# 문자열 반복
"""
import sys

T = int(sys.stdin.readline().rstrip())

list = []
for _ in range(T):
    N, S = sys.stdin.readline().rstrip().split()
    N = int(N)
    for i in S:
        for _ in range(N):
            list.append(i)
    list.append('\n')

for i in list:
    if i == '\n':
        print('')
    else:
        print(i, end='')
"""

# 단어의 개수
"""
import sys

S = sys.stdin.readline().rstrip().split()
print(len(S))
"""

# 상근이
"""
import sys

A, B = sys.stdin.readline().rstrip().split()

A = int(A[::-1])
B = int(B[::-1])
if A > B:
    print(A)
else:
    print(B)
"""

# 다이얼
"""
import sys

dic = {'A':2, 'B':2, 'C':2
       , 'D':3, 'E':3, 'F':3
       , 'G':4, 'H':4, 'I':4 
       , 'J':5, 'K':5, 'L':5
       , 'M':6, 'N':6, 'O':6
       , 'P':7, 'Q':7, 'R':7, 'S':7
       , 'T':8, 'U':8, 'V':8
       , 'W':9, 'X':9, 'Y':9, 'Z':9}

S = sys.stdin.readline().rstrip()

total = 0
for i in S:
    total += dic[i] + 1

print(total)
"""

# 킹, 퀸, 룩, 비숍, 나이트, 폰
"""
import sys
llist = [1,1,2,2,2,8]

S = sys.stdin.readline().rstrip().split()
totallist = []
cnt = 0
for i in S:
    totallist.append(llist[cnt] - int(i))
    cnt+=1

for i in totallist:
    print(i, end=' ')
"""

# 별 찍기
"""
import sys
N = int(sys.stdin.readline().rstrip())

spacebar = N -1 # 빈칸 찍는 변수
star = 1 # 별 찍는 변수

for i in range(N):
    for _ in range(spacebar):
        print(" ", end='')
    for _ in range(star):
        print("*", end='')
    spacebar -= 1
    star += 2
    print("")

star -= 4
spacebar += 2

for i in range(N-1):
    for j in range(spacebar):
        print(" ", end='')
    for _ in range(star):
        print("*", end='')
    spacebar += 1
    star -= 2
    print("")
"""

# 펠린드룸인지 확인하기
"""
import sys
S = sys.stdin.readline().rstrip()

if S == S[::-1]:
    print(1)
else:
    print(0)
"""


# 단어 공부
"""
import sys
S = sys.stdin.readline().rstrip()

for i in len(S):
    S[i].count
"""

# 크로아티아 알파벳
"""
import sys
alphabet = sys.stdin.readline().rstrip()
count = 0
my_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in my_list:
    if alphabet.count(i) > 0:
        count += alphabet.count(i)
        alphabet = alphabet.replace(i, '/')
        
alphabet = alphabet.replace('/', '')
print(len(alphabet) + count)
"""

# 행렬 덧셈
"""
import sys

def sumMatrix(A,B):
    answer = []

    for i in range(len(A)):
        tmp = []
        for j in range(len(A[i])):
            tmp.append(A[i][j] + B[i][j])
            print(A[i][j] + B[i][j], end=" ")

        print("")
        #answer.append(tmp)

N, M = map(int, sys.stdin.readline().rstrip().split())

A = [x for x in range(N)]
B = [x for x in range(N)]

for i in range(N):
    A[i] = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(N):
    B[i] = list(map(int, sys.stdin.readline().rstrip().split()))

sumMatrix(A, B)
"""

# 최대값
import sys

MATRIX = 9

dic = {'max' : 0, 'column' : 0, 'row' : 0}

def findMax():
    compare = -1
    for i in range(MATRIX):
        for j in range(MATRIX):
            if A[i][j] > compare:
                dic['max'] = A[i][j]
                compare = A[i][j]
                dic['row'] = i+1
                dic['column'] = j+1
    print(dic['max'])
    print(dic['row'], dic['column'])

A = [x for x in range(MATRIX)]

for i in range(MATRIX):
    A[i] = list(map(int, sys.stdin.readline().rstrip().split()))

findMax()