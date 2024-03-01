import requests
import time
import random
import json
import pandas as pd
import numpy as np
import plotly
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



## General Deck Calculations

<|toggle|theme|>

This page is designed to provide baseline information about the 

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
cardnamelist = ["Flickerwisp", "Worldfire","Solve the Equation", "Kangee, Sky Warden","Moorland Haunt", "Gavony Township", "Archon of Coronation", "Kiora Bests the Sea God", "Swamp", "Silverquill Command", "Sol Ring", "Black Lotus"]
cardname = random.choice(cardnamelist)
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
    typ = response_data["data"][0]["type_line"]
    oracle = response_data["data"][0]["oracle_text"]
    url = response_data["data"][0]["image_uris"]["large"]


    if "Land" in typ:
        manacost = "None"
    else:
        manacost = response_data["data"][0]["mana_cost"]

    if "Creature" in typ:
        power = response_data["data"][0]["power"]
        toughness = response_data["data"][0]["toughness"]
    else:
        power = "None"
        toughness = "None"
        
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

page2_md="""


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

Mana Cost:  <|{manacost}|>
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







#Page 3 combos
# ====================================================================================
cardcsv = None
carddf = pd.DataFrame()
carddf["Card Name"] =  "None"
carddf["Converted Mana Cost"] = "None"
carddf["Mana Cost"] =  "None"
carddf["Type"] = "None"
carddf["Oracle Text"] =  "None"
carddf["Power (if creature)"] =  "None"
carddf["Toughness (if creature)"] = "None"

namelist, cmclist, manalist, typlist, oraclelist, powerlist, toughnesslist = [],[],[],[],[],[],[]

def testfunc(state):
    print(state.cardcsv)
    if ".csv" in state.cardcsv:
        df = pd.read_csv(state.cardcsv)
    if ".xlsx" in state.cardcsv:
        df = pd.read_excel(state.cardcsv)

    notify(state,"info", "Loading Card information, please wait a few seconds.")

    for i in df[df.columns[0]]:
        print(i)
        try:
            nm, cmc, manacost, typ, oracle, power, toughness, url = scryfall_q(i)
        except: 
            namelist.append(i)
            cmclist.append("Error")
            manalist.append("Error")
            typlist.append("Error")
            oraclelist.append("Error")
            powerlist.append("Error")
            toughnesslist.append("Error")
            continue
        # print(nm, cmc, manacost, typ, oracle, power, toughness, url)
        state.namelist.append(nm)
        state.cmclist.append(cmc)
        state.manalist.append(manacost)
        state.typlist.append(typ)
        state.oraclelist.append(oracle)
        state.powerlist.append(power)
        state.toughnesslist.append(toughness)

    # print(cmclist, manalist, typlist, oraclelist, powerlist, toughnesslist)
    df2 = pd.DataFrame()
    df2["Card Name"] = state.namelist
    df2["Converted Mana Cost"] = state.cmclist
    df2["Mana Cost"] = state.manalist
    df2["Type"] = state.typlist
    df2["Oracle Text"] = state.oraclelist
    df2["Power (if creature)"] = state.powerlist
    df2["Toughness (if creature)"] = state.toughnesslist

    state.carddf = df2

    return
    

def analysis(state):
    print("Button pressed")



    #Mana Analysis
    notify(state, "info", "Now running analyses on Manabase")
    time.sleep(3)

    #Mana Curve Analysis
    notify(state, "info", "Now running analysis on Mana Curve")
    time.sleep(3)

    #Analysis of card types
    notify(state, "info", "Now running analysis of card types")
    time.sleep(3)

    #Analysis of card usages 
    notify(state, "info", "Now running card usage analysis")
    time.sleep(3)




    return

# ====================================================================================


page3_md="""



### Deck Uploads

<|layout|columns=1 1|
<| 
Please upload a csv of your deck in the following file uploader. You should see it detailed below. Please format your csv to just be a list of card names. 
|>

<| 
<|{cardcsv}|file_selector|label=Select File|on_action=testfunc|extensions=.csv,.xlsx|drop_message=Drop Message|>
|>

|>
<br/> <br/>


<|{carddf}|table|rebuild|editable=True|page_size=10|filter[Card Name]=True|filter[Converted Mana Cost]=True|filter[Mana Cost]=True|filter[Type]=True|filter[Power (if creature)]=True|filter[Toughness (if creature)]=True|>


<br/> <br/>

<|layout|columns=1 1|

<| 
Once the information within your deck above appears correctly, you can press the button on the right to run some baseline analysis of your deck.
|>

<| 
<|Show Deck Analyses|button|on_action=analysis|>
|>

|>

<br/> <br/>








"""







# <|Update Card|button|on_action=action3|> 












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
