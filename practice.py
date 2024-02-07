from taipy.gui import Gui, notify
import pandas as pd

# data = {"x_col": [0, 1, 2], "y_col1": [4, 1, 2]}
# data2 = {"x_col": [0, 1, 2], "y_col_1": [4, 2, 1], "y_col_2": [3, 1, 2]}
text = "Example Text"

dataframe = pd.DataFrame({"Text":['Test', 'Other', 'Love'],
                          "Score Pos":[1, 1, 4],
                          "Score Neu":[2, 3, 1],
                          "Score Neg":[1, 2, 0],
                          "Overall":[0, -1, 4]})

property_chart = {"type": "bar",
                  "x": "Text",
                  "y[1]": "Score Pos",
                  "y[2]": "Score Neu",
                  "y[3]": "Score Neg",
                  "y[4]": "Overall",
                  "color[1]": "green",
                  "color[2]": "grey",
                  "color[3]": "red",
                  "type[4]": "line"
                 }
page = """

# Getting started with Taipy GUI

My text: <|{text}|>

<|{text}|input|>

<|Run local|button|on_action=on_button_action|>


<|{dataframe}|chart|properties={property_chart}|>
"""


Gui(page).run() #use_reloader=True

# My number: <|{slider}|>

# <|{slider}|slider|min=1|max = 50|>


# def on_button_action(state):
#     notify(state, 'info', f'The text is: {state.text}')
#     state.text = "Button Pressed"

# def on_change(state, var_name, var_value):
#     if var_name == "text" and var_value == "Reset":
#         state.text = ""
#         return

# <|{data}|chart|x=x_col|y=y_col1|>

# <|{data2}|chart|x=x_col|y[1]=y_col_1|y[2]=y_col_2|>

# <|{data2}|chart|x=x_col|y[1]=y_col_1|y[2]=y_col_2|color[1]=green|>

# <|{data2}|chart|x=x_col|y[1]=y_col_1|y[2]=y_col_2|type[1]=bar|>