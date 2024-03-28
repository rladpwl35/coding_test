import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

veloc_list = []
test_list = []
for i in range(N):
    length, veloc = list(map(int, input().split()))
    veloc_list += [veloc] * length

for i in range(M):
    length, veloc = list(map(int, input().split()))
    test_list += [veloc] * length

diff = []

for i, j in zip(veloc_list, test_list):
    if j > i:
        diff.append(j-i)
    else:
        diff.append(0)

print(max(diff))

#https://softeer.ai/practice/6270
#소프티어는 대부분 구현인듯 하다.