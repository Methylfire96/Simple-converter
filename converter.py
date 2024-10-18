import PySimpleGUI as sg
    #enable_events = True, aktiviert bereiche zum anklicken für weitere events
layout = [
    [sg.Spin(["km to mile",
              "kg to pound",
              "sec to min",
              "meter to feet",
              "meter to yards",
              "km to sea miles"], key="-UNITS-")],
    [sg.Input(key="-INPUT-"),
     sg.Button("convert", key="-CONVERT-")],
    [sg.Text("Output", key="-OUTPUT-")]
]

window = sg.Window("Converter ++", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-CONVERT-":
        input_value = values["-INPUT-"]
        if input_value.isnumeric():
            match values["-UNITS-"]:
                case "km to mile":
                    output = round(float(input_value) * 0.6214, 2)
                    output_string = f"{input_value} km are {output} miles."

                case "kg to pound":
                    output = round(float(input_value) * 2.20462, 2)
                    output_string = f"{input_value} kg are {output} pounds."

                case "sec to min":
                    output = round(float(input_value) /60, 2)
                    output_string = f"{input_value} seconds are {output} minutes."

                case "meter to feet":
                    output = round(float(input_value) / 3.28084, 2)
                    output_string = f"{input_value} meter are {output} feet."

                case "meter to yards":
                    output = round(float(input_value) * 1.2, 2)
                    output_string = f"{input_value} meter are {output} yards."

                case "km to sea miles":
                    output = round(float(input_value) * 0.5399, 2)
                    output_string = f"{input_value} km are {output} sea miles."

            window["-OUTPUT-"].update(output_string)

window.close()