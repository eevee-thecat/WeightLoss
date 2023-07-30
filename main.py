from datetime import date

def calcBMI():
    print(
        "Body mass index (BMI) is a measure of body fat based on weight and height. To get your BMI, please answer "
        "the following questions:")
    height = input("What is your height to the nearest cm? ")
    try:
        height = int(height)
    except ValueError:
        print("Please make sure to enter a number.")

    weight = input("What is your weight in kg? ")
    try:
        weight = float(weight)
    except ValueError:
        print("Please make sure to enter a number.")

    bmi = weight / ((height / 100) ** 2)

    if bmi >= 30:
        status = "obese"
    elif bmi > 24.9:
        status = "overweight"
    elif bmi > 18.5:
        status = "normal weight"
    else:
        status = "underweight"

    print(f"Your BMI is {'{:.1f}'.format(bmi)}. This means that you are {status}.\n")

    input("Type anything to return to the menu. ")

def risks_of_overweight():
    print("""Individuals who are overweight or obese are at an increased risk for many serious diseases and health conditions such as heart disease, 
type 2 diabetes, and even cancer (CDC, 2022). Around 3 in 4 adults in the United States are either overweight or obese, which can lead to serious 
health issues (NIH, 2022).

A modest weight loss of 5-10% of your body weight can improve your blood pressure, cholesterol level, and risk for type 2 diabetes (Ryan & Yockey, 2018). 
A modest weight loss has also been associated with improvements in quality of life measures, which increases with additional weight loss (Ryan & Yocky, 2018). 


References: 
Centres for Disease Control and Prevention. (2022). Health Effects of Overweight and Obesity. Retrieved from: 
    https://www.cdc.gov/healthyweight/effects/index.html

National Heart, Lung, and Blood Cancer Institute. (2022). Overweight and Obesity: What are Overweight and Obesity? Retrieved from: 
    https://www.nhlbi.nih.gov/health/overweight-and-obesity

Ryan, D. & Yockey, S. (2018). Weight Loss and Improvement in Comorbidity: Differences at 5%, 10%, 15%, and Over. Curr Obes Rep. 2017 Jun; 6(2): 187-194.
    Retrieved from: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5497590/\n
""")

    input("Type anything to return to the menu. ")

def calories_current_weight():
    print("In order to determine how many calories you need to consume to maintain your current weight, please answer "
          "the following questions: ")

    invalid = True
    while invalid:
        invalid = False
        gender = input("Enter '1' if you are Female. Enter 2 if you are 'Male'. ")
        try:
            gender = int(gender)
        except ValueError:
            print("That's not a valid option. Please try again.")
            invalid = True

        if not invalid:
            if gender != 1 and gender != 2:
                print("That's not a valid option. Please try again.")
                invalid = True

    invalid = True
    while invalid:
        invalid = False
        height = input("What is your height to the nearest cm? ")
        try:
            height = int(height)
        except ValueError:
            print("Please make sure to enter a number.")
            invalid = True

        if not invalid:
            if height < 0:
                print("Please enter a positive number.")
                invalid = True

    invalid = True
    while invalid:
        invalid = False
        weight = input("What is your weight in kg? ")
        try:
            weight = float(weight)
        except ValueError:
            print("Please make sure to enter a number.")
            invalid = True

        if not invalid:
            if weight < 0:
                print("Please enter a positive number.")
                invalid = True

    invalid = True
    while invalid:
        invalid = False
        age = input("How old are you? ")
        try:
            age = int(age)
        except ValueError:
            print("Please make sure to enter a number.")
            invalid = True

        if not invalid:
            if age < 0:
                print("Please enter a positive age.")
                invalid = True

    if gender == 1:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5

    invalid = True
    while invalid:
        invalid = False
        activity_level = input("""Which of these options best describes your activity level?
Little to no exercise. Enter '1'.
Light exercise. Enter '2'.
Moderate exercise. Enter '3'.
Intense exercise. Enter'4'. \n""")

        try:
            activity_level = int(activity_level)
        except ValueError:
            print("That is not a valid option. Try again.")
            invalid = True

        if activity_level > 4 or activity_level < 1:
            print("That is not a valid option. Try again.")
            invalid = True

    if activity_level == 1:
        final_bmr = bmr * 1.2
    elif activity_level == 2:
        final_bmr = bmr * 1.375
    elif activity_level == 3:
        final_bmr = bmr * 1.55
    elif activity_level == 4:
        final_bmr = bmr * 1.725

    print(f"To sustain your current weight, you will need to consume {int(final_bmr)} calories daily.\n")

    input("Type anything to return to the menu. ")

    return final_bmr, weight


def daily_intake(bmr, current_weight):
    # invalid = True
    # while invalid:
    #     invalid = False
    #     current_weight = input("What is your weight in kg? ")
    #     try:
    #         current_weight = float(current_weight)
    #     except ValueError:
    #         print("Please make sure to enter a number.")
    #         invalid = True
    #
    #     if not invalid:
    #         if current_weight < 0:
    #             print("Please enter a positive number.")
    #             invalid = True

    invalid = True
    while invalid:
        invalid = False
        ideal_weight = input("What is the weight you want to reach? ")

        try:
            ideal_weight = int(ideal_weight)
        except ValueError:
            print("Please make sure to enter a number.")
            invalid = True

        if invalid == False and int(ideal_weight) < 0:
            print("Please enter a positive number. ")
            invalid = True

    invalid = True
    while invalid:
        invalid = False
        days_to_goal = input("In how many days would you like to reach your weight goal? ")

        try:
            days_to_goal = int(days_to_goal)
        except ValueError:
            print("Please make sure to enter a number.")
            invalid = True

        if invalid == False and int(days_to_goal) < 0:
            print("Please enter a positive number. ")
            invalid = True

    weight_to_lose = current_weight - ideal_weight
    weight_to_lose_per_day = weight_to_lose / days_to_goal
    calories_to_lose_per_day = weight_to_lose_per_day*3500
    daily_intake = bmr - calories_to_lose_per_day

    print(f"In order to reach the weight of {ideal_weight}kg in {days_to_goal} days, you will need to eat no more than {round(daily_intake)} calories per day.\n")

    input("Type anything to return to the menu. ")

def menu():
    have_bmr = False
    while True:
        print(
            """
0. Exit program.
1. Am I in a healthy weight range? 
2. What are the risks of being overweight? 
3. How many calories does my body need to maintain my current weight?
4. How many calories should I intake daily if I want to reach my weight goal? 
"""
        )
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            print("Error: Please select a valid menu entry")
            continue

        if not 0 <= choice <= 4:
            print("Error: Please select a valid menu entry")
            continue

        if choice == 0:
            print("Goodbye!")
            exit(0)
        elif choice == 1:
            calcBMI()
        elif choice == 2:
            risks_of_overweight()
        elif choice == 3:
            bmr, weight = calories_current_weight()
            have_bmr = True
        elif choice == 4 and have_bmr:
            daily_intake(bmr, weight)
        elif choice == 4 and not have_bmr:
            print("""The amount of calories needed to maintain your current weight is needed to calculate the daily calorie intake required to reach your weight goal. 
Please complete option 3 before choosing option 4.\n""")

            input("Type anything to return to the menu. ")


def main():
    menu()


if __name__ == '__main__':
    main()
