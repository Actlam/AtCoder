K, N = map(int,input().split())
A = list(map(int, input().split()))
List = []

for i in range(1, N):
  List.append(A[i] - A[i-1])

d = K - A[-1] + A[0]
List.append(d)
List.sort()
print(sum(List[:-1]))
