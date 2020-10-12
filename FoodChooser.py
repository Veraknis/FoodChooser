import random
# Make a healthy/Junk food picker program using Python3.7

# Creating 2 lists for the Healthy selection
_healthyFood = ['Apple', 'Pear', 'Peach',
                'Kale', 'Salad', 'Berries', 'Mushrooms']
_healthyDrink = ['Water', 'GreenTea', 'Tea', 'SoftDrink']

# Creating 2 lists for the junk selection
_JunkFood = ['Cake', 'Doritos', 'Chocolate', 'Crisps',
             'Cheese', 'Cheetos', 'Salted Peanuts', 'Ramen Noodles']
_JunkDrink = ['Coke', 'EnergyDrink', 'Wine', 'Beer', 'IronBru']


# Input prompt for user, taking the needed info from the user (Healthy/Junk Food choices) and name.
_userName = input("Please enter your name ")
_userFoodChoice = input(
    "Would you like a Healthy or Junk selection of food/drink? ")
# Print function to Address the user directly, calling the _userName Variable.
print("Hi " + _userName)

# This is the way I got it to work, nested if statements and using the random lib/ran.choice method.
# Used the OR operator here to account for using caps or not.
if _userFoodChoice == "Junk":
    print("The computer thinks you should drink some.. ")
    print(random.choice(_JunkDrink))
    if _userFoodChoice == "Junk":
        print("and the computer thinks you should eat some.. ")
        print(random.choice(_JunkFood))

# Used to OR operator here to account for using caps or not.
if _userFoodChoice == "Healthy":
    print("The computer thinks you should drink some.. ")
    print(random.choice(_healthyDrink))
    if _userFoodChoice == "Healthy":
        print("and the computer thinks you should eat some.. ")
        print(random.choice(_healthyFood))
