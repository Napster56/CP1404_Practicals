"""
CP1404/CP5632 Practical
Program looks up colour names and the hexadecimal colour code in a dictionary.
"""

COLOUR_NAMES = {"AntiqueWhite": "#faebd7", "aquamarine4": "#458b74", "azure3": "#c1cdcd", "BlueViolet": "#8a2be2",
               "CadetBlue": "#5f9ea0", "DarkOrange": "#ff8c00", "DarkOliveGreen": "#556b2f", "DarkOrchid": "#9932cc",
                "DarkSeaGreen": "#8fbc8f", "firebrick": "#b22222"}
for colour in COLOUR_NAMES:
    print("{:16} is {}".format(colour, COLOUR_NAMES[colour]))

colour = input("Enter the colour name: ").lower()
while colour != "":
    if colour in COLOUR_NAMES:
        print("The hexadecimal colour code for {} is {}".format(colour, COLOUR_NAMES[colour]))
    else:
        print("Invalid colour name")
    state = input("Enter the colour name: ").lower()
