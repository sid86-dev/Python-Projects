# AGE CALCULATOR PROJECT
def agecal(x, y):
    add = 2021-y
    age = x-add
    if age >=0:
        print(f'You will be {age} years old')
    else:
        print("\nENTER A VALID YEAR VALUE!!")


while True:
    print("""
     --------------------
       Age Calculator
    --------------------   """)
    input_ = input("Enter you age/Date of Birth: ")
    no = len(input_)
    # if 100 years old
    if int(input_) == 100:
        print("\nYou are already 100 years old")
    # if more then 118 years old
    elif no == 3 and int(input_) > 118:
        print("\nYou already turned 100!!")
        print("\nYou seem to be the oldest person alive")
    # if more then 100 but less then 118 years old
    elif int(input_) < 118 and int(input_) > 100:
        print("\nYou already turned 100!!")
    # if input is age
    elif no <= 2:
        age = int(input_)
        # if age more then 0 years
        if age >= 0:
            willbe = 100 - age
            print(f"\nYou will be 100 years old in {willbe} years")
            year = int(input("\nEnter a year where you want to check your age: "))
            agecal(year, age)
        # if age less then 0 years
        elif age < 0:
            print("\nYou are not yet born")
    elif no >= 4:
        age = 2021 - int(input_)
        # if age less then 0 years
        if int(input_) > 2021:
            print("\nYou are not yet born")
        # if age more then 0 years
        elif int(input_) < 2021:
            willbe = 100 - age
            print(f"\nYou will be 100 years old in {willbe} years")
            year = int(input("\nEnter a year where you want to check your age: "))
            agecal(year, age)
    # if equals to 118 years
    elif int(input_) == 118:
        print("\nYou already turned 100!!")
        print("You seem to be the oldest person alive")

    else:
        print("\nENTER A VALID VALUE!!")

