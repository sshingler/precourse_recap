name = input("Hello! Please enter your name: ")
age_years = int(input("Please enter your age in years: "))
age_days = age_years * 365
age_weeks = age_days / 7

print("Hello "+ name + ", you are " + str(age_years) + " years old.")
print("That is equal to " + str(age_days) + " days, or " + str(age_weeks) + " weeks.")

