input_string = input("list some dam numbers seperated with a space:\n")
list = input_string.split()
print (list)
sum = 0 
for num in list:
        sum += int (num)
print("Sum =",sum)

