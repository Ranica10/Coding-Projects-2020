n = int(input())
word = str(input())

a = 0
b = 0

for x in range(n):
  if word[x] == "A":
    a += 1
  elif word[x] == "B":
    b += 1

if a > b:
  print("A")
elif b > a:
  print("B")
else:
  print("Tie")