#This program asks the customer for the amount of food and drink items they ordered and gives an receipt

#Variables of food and drinks cost
coffee = 5
muffin = 4
brownies= 3.5
lemonade = 4
tea = 3
tax = 0.06

print('My Coffee and Muffin Shop')

#Input from customer of how many items they ordered
#Float statement was added to convert user input into a float to resolve type error
n_coffee = float(input('Number of coffees bought? '))
n_muffins = float(input('Number of muffins bought? '))
n_brownies = float(input('Number of brownies bought bought? '))
n_lemonade = float(input('Number of lemonades bought? '))
n_tea = float(input('Number of teas bought? '))


#Forumulas to find subtotal, sales tax and total
subtotal = n_coffee * coffee + n_muffins * muffin + n_brownies * brownies + n_lemonade * lemonade + n_tea * tea
sales_tax = subtotal * tax
total = subtotal + (subtotal * tax)


#Prints out customer receipt of items they ordered, tax, total and thank you message
print('My Coffee and Muffin Shop Receipt')
print(n_coffee, 'Coffee at $5 each: $', n_coffee * coffee)
print(n_muffins, 'Muffins at $4 each: $', n_muffins * muffin)
print(n_brownies, 'Brownies at $3.5 each: $', n_brownies * brownies)
print(n_lemonade, 'Lemonade at $4 each: $', n_lemonade * lemonade)
print(n_tea, 'Tea at $3 each: $', n_tea * tea)

#round statement was added to prevent extra decminals places from being shown
print('6% tax: $', round(sales_tax, 2))
print('Total: $', total)
print('Thank you for shopping with us. Hope to see you again soon!')



