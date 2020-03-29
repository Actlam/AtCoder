X = int(input())

noguchi = X // 500
goen = X % 500 // 5

print(noguchi * 1000 + goen * 5)