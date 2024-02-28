import requests
import time
import random
import json
# Add a navbar to switch from one page to the other
from taipy.gui import Gui, navigate, notify
cardname = "Solve the Equation"


page="""
<|{cardname}|>
<br/>
<|{cardname}|input|>
<br/>
<|Update Card|button|on_action=on_button_action|>
"""

def on_button_action(state):
    notify(state, 'info', f'The Card Name is: {state.cardname}')
    state.cardname = cardname
    return

def on_change(state, var_name, var_value):
    if var_name == "cardname" and var_value == "Reset":
        state.cardname = ""
        return

Gui(page).run()
