weight_is_fine = False
while weight_is_fine is False:
    weight = input("Enter your weight: ").strip()
    quit_process(weight)
    weight_unit = input("Enter L (lbs) or K (kgs)").strip()
    quit_process(weight_unit)
    
    while weight_unit.upper() != "L" and weight_unit.upper() != "K":
        print("Enter a valid weight unit or quit to exit")
        weight_unit = input("Enter L (lbs) or K (kgs)").strip()
        quit_process(weight_unit)
    elif weight_unit.upper() == "L":
        try:
            weight_pounds = float(weight)
            weight_is_fine = True
            weight_kilograms = weight_pounds * 0.45359237
            print(f"Weight : {weight_kilograms} kg")
        except:
            print("Check your weight")
    elif weight_unit.upper() == "K":
        try:
            weight_kilograms = float(weight)
            weight_is_fine = True
            weight_pounds = weight_kilograms * 2.2046226218
            print(f"Weight : {weight_pounds} lbs")
        except:
            print("Check your weight")
# Quit process if quit action typed           
def quit_process(action):
    if action.upper == "QUIT":
        print(Bye bye)
        quit()