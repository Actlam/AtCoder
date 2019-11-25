S = input()
counter = 0
week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]

for i in week:
  if i == S:
    print(7 - counter)
    break
  counter+=1