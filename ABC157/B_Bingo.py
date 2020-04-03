# A1 = list(map(int, input().split()))
# A2 = list(map(int, input().split()))
# A3 = list(map(int, input().split()))

A = [list(map(int, input().split())) for i in range(3)]

N = int(input())
b = [(int(input())) for _ in range(N)]

bingo1 = [0, 0, 0]
bingo2 = [0, 0, 0]
bingo3 = [0, 0, 0]

# 穴を開ける工程
for i in range(3):
  for j in range(N):
    if A[i][0] == b[j]:
      bingo1[i] = 1
    if A[i][1] == b[j]:
      bingo2[i] = 1
    if A[i][2] == b[j]:
      bingo3[i] = 1
      

# ビンゴ判定
if bingo1[0] == bingo1[1] == bingo1[2] == 1:
    print("Yes")
elif bingo2[0] == bingo2[1] == bingo2[2] == 1:
    print("Yes")
elif bingo3[0] == bingo3[1] == bingo3[2] == 1:
    print("Yes")
elif bingo1[0] == bingo2[0] == bingo3[0] == 1:
    print("Yes")
elif bingo1[1] == bingo2[1] == bingo3[1] == 1:
    print("Yes")
elif bingo1[2] == bingo2[2] == bingo3[2] == 1:
    print("Yes")
elif bingo1[0] == bingo2[1] == bingo3[2] == 1:
    print("Yes")
elif bingo1[2] == bingo2[1] == bingo3[0] == 1:
    print("Yes")
else:
    print("No")

