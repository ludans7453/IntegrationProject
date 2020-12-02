import math  # It allows access to functions in the math library (module)
import datetime  # It gives access to datetime() class.
import os  # It allows the program to interact with the operating system.

"""Integration project for Lucas Andres, COP 1500
        __author__ = "Lucas Andres"

Welcome to the CalPYbara Calorie Counter!
This is a simple calorie counter to account for all
the numbers on the back of the label."""

"""Special thanks to Jairo Garciga for reviewing my code 
and being very helpful in general."""

"""Highly recommended to run twice. The first time using it creates a 
directory and three files are created within the directory. The second time
you run the program, you can choose 'Y' to see data from previous sessions.
This will open notepad (if you are using windows) displaying the information
from the file TotalConsumedCalories.txt"""

# All facts taken from
# “Capybara.” Facts, 20 Dec. 2018,
# www.nationalgeographic.com/animals/mammals/c/cabybara-facts/.
# General facts about capybaras.


# I created a function for the code below to separate
# functional code from the code that is being worked on
# and to make things easier to read.
date = datetime.datetime.now()
returning_user = input("If you would like to see your data from previous"
                       " sessions, press 'Y', otherwise press 'enter'.")
if returning_user == 'Y':
    os.system('CalPybara\TotalConsumedCalories.txt')
else:
    pass
# This gives an option to the user to see their previous input data.
# os.system('text file') opens up the txt file in the default text editor.
if not os.path.exists('CalPybara'):
    os.mkdir('CalPybara')
else:
    pass
# When used for the first time, the 'CalPybara' directory will not exist
# this ensures that the directory will be created and if the program
# is ran again, the directory will not be made again.
name = input("\nHello there! \nWhat's your name?: ")


def calculate_tdee():
    # packed the code in a function to separate it from the
    # rest of the code and condense it all.
    global daily_calorie_goal
    while True:
        try:
            weight = int(input("\nHow much do you weigh in pounds?: "))
        except ValueError:
            print("\nEnter a numerical value.")
        else:
            break
    if 77 <= weight <= 143:
        print("\nThere are Capybaras your size!")
    elif weight > 143:
        print(("\nYou weigh {} pounds more "
               "than the biggest Capybara!".format(weight - 143)))
        # the subtraction operator is used to find the
        # difference between a capybaras max weight and
        # the users weight.
    while True:
        try:
            height = int(input("\nWhat is your height in inches ?: "))
        except ValueError:
            print("\nEnter a numerical value.")
        else:
            break
    height = (height * .0254)
    # this converts height in inches to meters using the
    # multiplication (arithmetic) operator.
    height = int(height / 0.0254)
    # this converts height in meter back to inches
    # using the division (arithmetic) operator.
    if 55 < height < 3000:  # and boolean operator
        print(("\nWOW! That's approximately {} inches "
               "longer than a "
               "Capybara!".format(int((height * .0254 - 1.397) // .0254))))
        # a conversion that includes the floor
        # division arithmetic operator to
        # ensure the number is always a whole number.
    weight *= 0.45359237  # shortcut (assignment) operator.
    # This converts weight to kilograms for the equation.
    height *= 2.54  # shortcut (assignment) operator.
    # This converts inches to centimeters for the equation.
    while True:
        try:
            age = int(input("\nHow old are you?: "))
        except ValueError:
            print("\nEnter a numerical value.")
        else:
            break
    # Source for revised Harris-Benedict equation.
    # “Calculating Energy Expenditure.” Nutritional Assessment,
    # Maastricht University Medical Center+, 2020,
    # nutritionalassessment.mumc.nl/en/calculating-energy-expenditure.
    male_bmr = (88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age))
    # This is the revised Harris-Benedict Basal metabolic rate formula
    # for males using metric units.
    female_bmr = (447.593 + (9.247 * weight) + (3.098 * height) - (4.33 * age))
    # This is the revised Harris-Benedict basal metabolic rate formula for
    # females using metric units.
    # both equations make use of addition, multiplication
    # and subtraction arithmetic operators.
    while True:
        try:
            sex = int(input("\nAre you male or female? "
                            "Type '1' for male or '2' for female: "))
            while sex < 1 or sex > 2:
                print("\nEnter the whole number '1' or '2'")
                sex = int(input("\nAre you male or female? "
                                "Type '1' for male or '2' for female: "))
        except ValueError:
            print("\nEnter a numerical value.")
        else:
            break
    # The BMR formula differs depending on
    # whether the user is female or male.
    if sex == '1':
        sex = male_bmr
    else:
        sex = female_bmr
    while True:
        try:
            activity = int(input("\nFrom 1-5, 1 = not active and 5 = very "
                                 "active, "
                                 "how active are you ?: "))
            while activity < 1 or activity > 5:
                print("\nEnter a whole number between 1 and 5")
                activity = int(input("\nFrom 1-5, 1 = not active and 5 = "
                                     "very active, "
                                     "how active are you ?: "))
        except ValueError:
            print("\nEnter a whole number between 1 and 5.")
        else:
            break
    # The Harris Benedict equation requires an 'activity factor'
    # to determine total daily caloric need. Sourced from
    # “Calculating Energy Expenditure.” Nutritional Assessment,
    # Maastricht University Medical Center+, 2020,
    # nutritionalassessment.mumc.nl/en/calculating-energy-expenditure.
    while activity in range(1, 6):
        if activity == 1:
            activity = 1.2
        elif activity == 2:
            activity = 1.375
        elif activity == 3:
            activity = 1.55
        elif activity == 4:
            activity = 1.725
        elif activity == 5:
            activity = 1.9
        else:
            print(activity)
        print("\nYour total daily caloric need is",
              int(sex * activity), "calories.")
        daily_calorie_goal = int(sex * activity)
        print("\nTime for another fun fact! Female capybaras average",
              (44 % 10), "to", (55 % 10), "pups per litter.")
    # modulus operator is used to represent the number of pups per litter
    # as the result needed is represented as the remainder
    # The output shows total daily caloric need. As always,
    # topics involving human
    # biology are nuanced and generally are not the most
    # precise but the Harris Benedict
    # equation is widely used as an estimate.
    return daily_calorie_goal


def capy_age(age):
    # a function that accepts a parameter and uses local variables (non-global)
    sqr_root = math.sqrt(age)
    reverse_root = int(sqr_root ** 2)
    return reverse_root


# Function creation for same reason as def calculate_tdee
def greeting():
    print("\nGlad to have you", name + "!" * 3)
    # here the '+' is used for concatenation and '*' is used
    # to multiply the string "!" so it prints 3 times.
    print("\nWelcome to CalPybara, the Python calorie counter that is "
          "weirdly influenced by capybaras!")
    print("\nFun fact: Did you know that anacondas "
          "(a type of constrictor, like pythons) are a natural predator"
          " to capybaras?")
    print("\nTo get started using CalPYbara, "
          "more information is needed.")
    print("\nBut first, another fact! The average age of "
          "capybaras is", capy_age(7), "years old.")
    # capy_age() is a call to the function that accepts a parameter.


def breakfast_data():
    # This function creates a file and
    calorie_breakfast = open("CalPybara/breakfastInput.txt", 'w')
    # 'w' ensures that with every iteration of the program, the data inside
    # the files in the CalPybara directory are replaced with new values.
    print("\nThe following reflects what you have eaten for breakfast.")
    for info in range(1, 100):
        # Used a for loop set with a range of 1-99 and an if condition
        # to allow the user to enter as many values as they would like.
        # highly unlikely a user would input so many items for one meal
        while True:
            try:
                cal_val = int(input("\nEnter caloric value "
                                    "of the food item: "))
            except ValueError:
                print("\nInput a numerical value.")
            else:
                break
        cal_val = str(cal_val)
        calorie_breakfast.write(cal_val)
        calorie_breakfast.write(" ")
        move_on = input("\nType 'Y' to enter more, otherwise press enter.")
        if move_on == "Y":
            continue
        else:
            break
    calorie_breakfast.close()
    # This allows the user to input the calorie values and control how many
    # times they would like to enter individual values.
    # A file is created in the CalPybara directory that was made in the
    # beginning to store the input data. The data is stored with a space
    # in between values and on one line.


def lunch_data():
    # This function creates a file and
    calorie_lunch = open("CalPybara/lunchInput.txt", 'w')
    # 'w' ensures that with every iteration of the program, the data inside
    # the files in the CalPybara directory are replaced with new values.
    print("\nThe following reflects what you have eaten for lunch.")
    for info in range(1, 100):
        # Used a for loop set with a range of 1-99 and an if condition
        # to allow the user to enter as many values as they would like.
        # highly unlikely a user would input so many items for one meal
        while True:
            try:
                cal_val = int(input("\nEnter caloric value of the "
                                    "food item: "))
            except ValueError:
                print("\nInput a numerical value.")
            else:
                break
        cal_val = str(cal_val)
        calorie_lunch.write(cal_val)
        calorie_lunch.write(" ")
        move_on = input("\nType 'Y' to enter more, otherwise press enter.")
        if move_on == "Y":
            continue
        else:
            break
    calorie_lunch.close()
    # This allows the user to input the calorie values and control how many
    # times they would like to enter individual values.
    # A file is created in the CalPybara directory that was made in the
    # beginning to store the input data. The data is stored with a space
    # in between values and on one line.


def dinner_data():
    # This function creates a file and
    calorie_dinner = open("CalpyBara/dinnerInput.txt", 'w')
    # 'w' ensures that with every iteration of the program, the data inside
    # the files in the CalPybara directory are replaced with new values.
    print("\nThe following reflects what you have eaten for dinner.")
    for info in range(1, 100):
        # Used a for loop set with a range of 1-99 and an if condition
        # to allow the user to enter as many values as they would like.
        # highly unlikely a user would input so many items for one meal
        while True:
            try:
                cal_val = int(input("\nEnter caloric value "
                                    "of the food item: "))
            except ValueError:
                print("\nInput a numerical value.")
            else:
                break
        cal_val = str(cal_val)
        calorie_dinner.write(cal_val)
        calorie_dinner.write(" ")
        move_on = input("\nType 'Y' to enter more, otherwise press enter.")
        if move_on == "Y":
            continue
        else:
            break
    calorie_dinner.close()
    # This allows the user to input the calorie values and control how many
    # times they would like to enter individual values.
    # A file is created in the CalPybara directory that was made in the
    # beginning to store the input data. The data is stored with a space
    # in between values and on one line.


def breakfast_cals():
    # declaring the variable within the function to avoid scope warning
    data = 0
    breakfast_file = open("CalPybara/breakfastInput.txt", "r")
    for data in breakfast_file:
        data = data.rsplit()
    breakfast_file.close()
    for num in range(0, len(data)):
        data[num] = int(data[num])
    breakfast_result = sum(data)
    return breakfast_result
    # The file opens in 'r' (read only) and using a for loop, reads the values
    # in the line, separates them into a list and then converts the values in
    # the list from strings to integers so the sum function can be used.


def lunch_cals():
    # declaring the variable within the function to avoid scope warning
    data = 0
    lunch_file = open("CalPybara/lunchInput.txt", "r")
    for data in lunch_file:
        data = data.rsplit()
    lunch_file.close()
    for num in range(0, len(data)):
        data[num] = int(data[num])
    lunch_result = sum(data)
    return lunch_result
    # The file opens in 'r' (read only) and using a for loop, reads the values
    # in the line, separates them into a list and then converts the values in
    # the list from strings to integers so the sum function can be used.


def dinner_cals():
    data = 0
    # declaring the variable within the function to avoid scope warning
    dinner_file = open("CalPybara/dinnerInput.txt", "r")
    for data in dinner_file:
        data = data.rsplit()
    dinner_file.close()
    for num in range(0, len(data)):
        data[num] = int(data[num])
    dinner_result = sum(data)
    return dinner_result
    # The file opens in 'r' (read only) and using a for loop, reads the values
    # in the line, separates them into a list and then converts the values in
    # the list from strings to integers so the sum function can be used.


greeting()

tdee_question = input("\nDo you know your daily calorie goal? "
                      "Type 'Y' for yes or 'N' for no: ")
if tdee_question != "N":  # Does not equal relational operator
    # TDEE = Total Daily Energy Expenditure.
    while True:
        try:
            daily_calorie_goal = int(input("\nGreat! What is your calorie "
                                           "goal? "))
        except ValueError:
            print("You need to enter a numerical value.")
        else:
            break
    while daily_calorie_goal < 500 or daily_calorie_goal > 5000:
        calorie_check = input("\nAre you sure? That's outside the "
                              "average caloric goal."
                              "Type 'Y' for yes or 'N' for no: ")
        if calorie_check == "Y":
            break
        elif calorie_check == "N":
            while True:
                try:
                    daily_calorie_goal = int(
                        input("\nGreat! What is your calorie "
                              "goal? "))
                except ValueError:
                    print("\nYou need to enter a numerical value.")
                else:
                    break
    # import math is used to access the sqrt function to take the
    # square root of 7 and then use exponentiation to return it
    # to its original value. int() is used to ensure a float value
    # is not returned.
else:
    print("\nNo problem! Let's figure that out.")
    daily_calorie_goal = calculate_tdee()
    # From here I require specific information to calculate TDEE.
    # It will all be plugged into the revised Harris Benedict Equation.
    # Revised in 1984 by A M Roza and H M Shizgal.
# From here, the program will need to add the calories
# input by the user and notify the user when
# they are within 500 calories of their daily goal and when
# they exceed their daily goal.
print("\nFrom this point you will need to provide the calorie "
      "\ninfo and Calpybara will store it for you.")

breakfast_data()
total_breakfast_cals = breakfast_cals()  # saves the sum of the input data
lunch_data()
total_lunch_cals = lunch_cals()  # save the sum of the input data
dinner_data()
total_dinner_cals = dinner_cals()  # saves the sum of the input data

total_consumed_calories = (total_breakfast_cals + total_lunch_cals
                           + total_dinner_cals)
#  gathers all the input calorie data to compare it to the TDEE.
if total_consumed_calories == daily_calorie_goal:
    # if this condition is met, the txt file is opened to append new data.
    # the date, which is formatted to include the weekday, day, month and year,
    # and the total calories consumed for the session.
    print("\nWow! You met your daily calorie goal!")
    all_calories = open("CalPybara/TotalConsumedCalories.txt", 'a')
    date = date.strftime("%A, %b " + "%d, %Y")
    # allows for date formatting. Using the date = datetime.datetime.now
    # from earlier in the program
    all_calories.write("{} Calories "
                       "consumed: {}".format(date, daily_calorie_goal))
    all_calories.write("\n")
    all_calories.close()
elif total_consumed_calories < daily_calorie_goal:
    # if this condition is met, the txt file is opened to append new data.
    # the date, which is formatted to include the weekday, day, month and year,
    # and the total calories consumed for the session.
    below_goal = (daily_calorie_goal - total_consumed_calories)
    print("\nYou consumed", below_goal, "less than your daily "
                                        "calorie goal.")
    all_calories = open("CalPybara/TotalConsumedCalories.txt", 'a')
    date = date.strftime("%A, %b " + "%d, %Y")
    all_calories.write("{} Calories "
                       "consumed: {}".format(date, total_consumed_calories))
    all_calories.write("\n")  # newline character for organization.
    all_calories.close()  # closes the file. A good practice.
else:
    above_goal = (total_consumed_calories - daily_calorie_goal)
    print("\nYou consumed", above_goal, "calories more than your daily "
                                        "calorie goal.")
    all_calories = open("CalPybara/TotalConsumedCalories.txt", 'a')
    date = date.strftime("%A, %b " + "%d, %Y")
    all_calories.write("{} Calories "
                       "consumed: {}".format(date, total_consumed_calories))
    all_calories.write("\n")
    all_calories.close()

print("\nCapybaras eat their own feces in the morning!"
      "\nHow can you track those calories?!?!")

print("\nThank you for using Calpybara!"
      "\nThe only Capybara Python calorie counter"
      "\nin existence! Your data has been stored.")
# I am confident that this is true. It has to be.
quit_program = input("\nType 'Enter' to exit program.")
# I noticed when the program is ran through C:\\WINDOWS\py.exe
# the program ends abruptly w/o giving the user a chance to read through it.
# so this was added to fix that.
