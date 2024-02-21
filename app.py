from taipy import Gui

# Add a navbar to switch from one page to the other
from taipy.gui import Gui, navigate, notify

root_md="<|menu|label=Menu|lov={[('Page-1', 'Page 1'), ('Page-2', 'Page 2'), ('Page-3', 'Page 3')]}|on_action=on_menu|>"


#Page 1 combos
# ====================================================================================

def on_button_action(state):
    notify(state, 'info', f'The text is: {state.average}')
    state.average = 0

def on_change(state, var_name, var_value):
    if var_name == "average" and var_value == "Reset":
        state.average = ""
        return


ncolors = 1


def colors():
    print(True)

def cleaning():
    print(True)


average = float(0.3)


# ====================================================================================

page1_md="""



## Page 1 - Deck Statistics

<|toggle|theme|>

<|layout|columns=1 1|
<|

<|{ncolors}|slider|min=1|max=5|>

Number of colors: <|{ncolors}|>

|>
<|

What is your average mana value?

<|{average}|input|>

Average: <|{average}|>

<|Reset|button|on_action=on_button_action|>


|>


|>



"""


#Page 2 combos
# ====================================================================================


# ====================================================================================


page2_md="""



## This is page 2



"""



#Page 3 combos
# ====================================================================================


# ====================================================================================

page3_md="""



## This is page 3




"""


def on_menu(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)

#comment this for sidebar
#------------------------------------------------------
# root_md = "<|navbar|>"
#------------------------------------------------------
    
pages = {
    "/": root_md,
    "Page-1": page1_md,
    "Page-2": page2_md,
    "Page-3": page3_md
}

Gui(pages=pages).run()

# My number: <|{slider}|>

# <|{slider}|slider|min=1|max = 50|on_change=on_slider|>


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

#<|Analyze|button|on_action=local_callback|>
