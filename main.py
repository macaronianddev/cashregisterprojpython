intro = "Cash Register Python Project by Creighton Whitaker"
print(intro)
requestCost = "Please enter the total cost in cents"
print(requestCost)
x = int(input())
print(x)
requestPay = "Please enter the total payment in cents"
print(requestPay)
y = int(input())
print (y)
z = x-y
if z == 0:
  print("No change required")
elif z>0:
  print(z, "cents needed")
  print(z//10000, "hundred dollar bills")
  z = z%10000
  print(z//5000, "fifty dollar bills")
  z = z%5000
  print(z//2000, "twenty dollar bills")
  z = z%2000
  print(z//1000, "ten dollar bills")
  z = z%1000
  print(z//500, "five dollar bills")
  z = z%500
  print(z//100, "one dollar bills")
  z = z%100
  print(z//25, "quarters")
  z = z%25
  print(z//10, "dimes")
  z = z%10
  print(z//5, "nickles")
  z = z%5
  print(z//1, "pennies")
elif z<0:
  a=abs(z)
  print(a, "cents owed")
  print(a//10000, "hundred dollar bills")
  a = a%10000
  print(a//5000, "fifty dollar bills")
  a = a%5000
  print(a//2000, "twenty dollar bills")
  a = a%2000
  print(a//1000, "ten dollar bills")
  a = a%1000
  print(a//500, "five dollar bills")
  a = a%500
  print(a//100, "one dollar bills")
  a = a%100
  print(a//25, "quarters")
  a = a%25
  print(a//10, "dimes")
  a = a%10
  print(a//5, "nickles")
  a = a%5
  print(a//1, "pennies")
