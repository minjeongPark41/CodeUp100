# 출석 번호 부르는 횟수
n = int(input())
# 무작위로 부른 n개의 숫자
# 예를 들어 위에서 n=5면 3,4,1,2,2 이렇게
# 그걸 공백 기준으로 잘라서 저장해주기
a = input().split()

for i in range(n): #0부터 n-1까지
    a[i] = int(a[i]) # int형으로 변환하기

#23명의 학생들에 대한 공간을 만들자
d = []
for i in range(24):
    d.append(0) # 0을 추가! 

#번호가 불러질 때마다 +1 증가시키기

for i in range(n):
    d[a[i]] +=1

for i in range (1,24):
    print(d[i], end='')

