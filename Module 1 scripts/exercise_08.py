# Aman Kumar
original_list = []
for i in range(10):
    num = int(input("Enter Number {}: ".format(i+1)))
    original_list.append(num)

unique_list = []
for num in original_list:
    if original_list.count(num) == 1:
        unique_list.append(num)

print("Original List:", original_list)
print("Nums that appear once:", unique_list)
