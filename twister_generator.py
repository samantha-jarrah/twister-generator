import random 

# Set up lists of limb and color options
limbs = ["Right Hand", "Left Hand", "Right Foot", "Left Foot"]
colors = ["Red", "Green", "Yellow", "Blue"]

# Produce random combination of limbs and colors
while True:
    limbChoice = random.choice(limbs)
    colorChoice = random.choice(colors)
    userInput = input("\n\nTo receive your Twister combination, press any key. To quit, input Q: ")

    if userInput.lower() == "q":
        break
    else:
        print(f"{limbChoice} on {colorChoice}")