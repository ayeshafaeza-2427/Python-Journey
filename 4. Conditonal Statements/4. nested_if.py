age = int(input("Enter your a : "))

if age >= 18:
    has_license = input("Do you have a driving license? (yes/no): ")

    if has_license.lower() == "yes":
        print("You can drive.")
    else:
        print("You can't drive without a license.")
else:
    print("You are not old enough to drive.")
