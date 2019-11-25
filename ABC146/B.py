N = int(input())
S = str(input())
ans = ""

for i in range(len(S)):
  ascii = (ord(S[i]) - ord('A') + N) % 26 + ord('A')
  ans += chr(ascii)
  
print(ans)