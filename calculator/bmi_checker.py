input_is_fine = False
while input_is_fine is False:
    weight_input = input("Enter your weight : ")
    try:
        weight = float(weight_input)
        height = float(height_input)
        input_is_fine = True
    except:
        print("Check your input")
if input_is_fine is True:
    bmi = weight / height**2
    print("Your BMI is", bmi)
