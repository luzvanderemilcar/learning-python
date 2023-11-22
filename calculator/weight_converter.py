# Quit process if quit action typed           
def quit_process(action):
    if action.upper() == "QUIT":
        print("Bye bye")
        quit()
        
lb_to_kg_factor = 0.45359237
kg_to_lb_factor = 2.2046226218

# control the success of Weight input
weight_is_fine = False
while weight_is_fine is False:
    print("Type 'quit' to exit")
    weight = input("Your weight : ").strip()
    quit_process(weight)
    weight_unit = input("Enter L (lb) or K (kg)").strip()
    quit_process(weight_unit)
    
    while weight_unit.upper() != "L" and weight_unit.upper() != "K":
        print("Enter a valid weight unit")
        weight_unit = input("Enter L (lb) or K (kg)").strip()
        quit_process(weight_unit)
    if weight_unit.upper() == "L" or weight_unit.upper() == "K":
        if weight_unit.upper() == "L":
            factor = lb_to_kg_factor
            final_unit = "Kilos"
        else:
            factor = kg_to_lb_factor 
            final_unit = "Pounds"
        try:
            weight_entered = float(weight)
            weight_is_fine = True
            weight_converted = weight_entered * factor
            print(f"Weight : {weight_converted} {final_unit}")
        except:
            print("Check your weight")