int(input("Enter a number"))

odd_numbers = []
for number in range(1, 100):  
    if number % 2 != 0:
        odd_numbers.append(number)

print(odd_numbers) 



# create the list
fruits = ["apple", "banana", "tomato", "mango", "orange"]

# capitalize the fruits and print the result:
capitalized_fruits = [i.capitalize() for i in fruits]
print(capitalized_fruits)

