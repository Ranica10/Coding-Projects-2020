num = int(input("Till what number do you want to end at: "))
i = 1

#Solved with while loop
while i <= num:
  if (i%5 == 0) and (i%3 == 0):
    print("fizzbuzz")
    i += 1
  elif (i%3 == 0):
    print("fizz")
    i += 1
  elif (i%5 == 0):
    print("buzz")
    i += 1
  else:
    print(i)
    i += 1
else:
  print("done")

#Solved with for loop
for i in range(num):
  i += 1
  if (i%5 == 0) and (i%3 == 0):
    i = "fizzbuzz"
    print(i)
  elif (i%3 == 0):
    i = "fizz"
    print(i)
  elif (i%5 == 0):
    i = "buzz"
    print(i)
  else:
    print(i)
else:
  print("done")