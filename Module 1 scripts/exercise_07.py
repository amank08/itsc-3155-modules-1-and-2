# Aman Kumar
list = []
while True:
    i = input("Enter a value or QUIT to quit: ")
    if i == "QUIT":
        break
    list.append(i)
print("All nums:", list)

evens = []
for num in list:
    if int(num) % 2 == 0:
        evens.append(num)
print("Even Nums:", evens)
