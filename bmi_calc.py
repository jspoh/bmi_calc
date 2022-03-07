# in case you're too lazy to do the manual calculation for your BMI
# also made this to learn pysimplegui

import PySimpleGUI as sg

print("Initializing program..")

sg.theme('DarkTeal9')

layout = [
    [sg.Text("Input data in the fields below")],
    [sg.Text("Height in meters", size=(15, 1)), sg.In(key="height")],
    [sg.Text("Weight in KG", size=(15, 1)), sg.In(key="weight")],
    [sg.Button("Calculate BMI"), sg.Button("Cancel")]
]

window = sg.Window("BMI calculator", layout)

running = True
while running:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        running = False
    if event == "Calculate BMI":
        try:
            weight = float(values["weight"])
            height = float(values["height"])
            BMI = weight / (height ** 2)
            BMI = float(str(BMI)[:5])
            cat = ""
            if BMI < 18.5:
                cat = "underweight"
            elif 18.5 <= BMI < 25:
                cat = "healthy"
            elif 25 <= BMI < 30:
                cat = "overweight"
            elif BMI >= 30:
                cat = "obese"
            sg.popup(f"Your BMI is {BMI}", f"You are {cat}")
        except ValueError:
            sg.popup("Please enter a valid weight/height!")
