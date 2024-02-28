import requests
import time
import random
import json
# Add a navbar to switch from one page to the other
from taipy.gui import Gui, navigate, notify

root_md="<|menu|label=Menu|lov={[('Page-1', 'Page 1'), ('Page-2', 'Page 2'), ('Page-3', 'Page 3')]}|on_action=on_menu|>"


#Page 1 combos
# ====================================================================================

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

def on_button_action(state):






    notify(state, 'info', f'The Card Name is: {state.average}')
    state.average = 1



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
<br/> <br/>
Average: <|{average}|>
<br/> <br/>
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
cardname = "Solve the Equation"
def scryfall_q(query, name = True,expac=False ):

    


    def make_api_call_with_delay(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()  # Assuming the response is JSON data
            else:
                print(f"Request failed with status code: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            return None
    

    if name == True:
        base_url = "https://api.scryfall.com/cards/search?q="
        search_query = query
        url = base_url + f'name:"{search_query}"'
    
    if expac == True:
        base_url = "https://api.scryfall.com/cards/search?q="
        search_query = query
        url = base_url + f'name:"{search_query}"'



    delay = random.uniform(0.05, 0.1)
    time.sleep(delay)
    response_data = make_api_call_with_delay(url)


    nm = response_data["data"][0]["name"]
    cmc = response_data["data"][0]["cmc"]
    manacost = response_data["data"][0]["mana_cost"]
    typ = response_data["data"][0]["type_line"]
    oracle = response_data["data"][0]["oracle_text"]
    if "Creature" in typ:
        power = response_data["data"][0]["power"]
        toughness = response_data["data"][0]["toughness"]
    else:
        power = "None"
        toughness = "None"
    url = response_data["data"][0]["image_uris"]["large"]
    # if response_data:
    #     print(json.dumps(response_data, indent=4))  
        
    return nm, cmc, manacost, typ, oracle, power, toughness, url

nm, cmc, manacost, typ, oracle, power, toughness, url = scryfall_q(cardname)


def on_button_action(state):
    notify(state, 'info', f'The Card Name is: {state.cardname}')

    nm, cmc, manacost, typ, oracle, power, toughness, url = scryfall_q(state.cardname)
    

    print(nm, cmc, manacost, typ, oracle, power, toughness, url)
    state.nm = nm
    state.cmc = cmc
    state.manacost = manacost
    state.typ = typ
    state.oracle = oracle
    state.power = power
    state.toughness = toughness
    state.url = url

    return

def on_change(state, var_name, var_value):
    if var_name == "cardname" and var_value == "Reset":
        state.cardname = ""
        return



# ====================================================================================

page3_md="""


## Scryfall API

This page serves as a test for the scryfall api and accessing this information

To use this page, please input a correct card name (correctly capitalized) in the below text box
<br/> <br/>
<|{cardname}|input|>
<br/> <br/>

<|Update Card|button|on_action=on_button_action|>

<br/>

=================================================================



Card information:
<br/>
=================================================================
<br/><br/>

Name:  <|{nm}|>
<br/> <br/> 

CMC:  <|{cmc}|>
<br/> <br/> 

Type:  <|{typ}|>
<br/> <br/> 

Textbox:  <|{oracle}|>
<br/>  <br/> 

Power (if creature):  <|{power}|>
<br/> <br/> 

Toughness (if creature):  <|{toughness}|>
<br/> <br/> 

Printed Card: 
<br/> 
<|{url}|image|>
<br/> 
=================================================================

"""
#Image display  <|{url}|image|>
#link: <a href:{url}>URL</a>
# <|Run API|button|on_action=buttonpress|>


def on_menu(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)

#comment this for sidebar
#------------------------------------------------------
# root_md = "<|navbar|>"
#------------------------------------------------------
  
#hi i proud of you :) <3



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
