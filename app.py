import requests
import time
import random
import json
import pandas as pd
import numpy as np
import plotly
from taipy.gui import Gui, navigate, notify, download


root_md = "<center>\n<|navbar|>\n</center>"
dur = 5000


##############################
###### Part A Variables #####
platform = "Moxfield"
moxinst = """
In order to download a deck from moxfield, follow the following steps:
"""
archinst = """
In order to download a deck from archidekt, follow the following steps:
"""
plaininst = """
In order to build a deck from scratch, follow the following steps:

"""
textresponse = ""


def textchanger(state):
    # notify(state, "info", "New platform selected", duration = dur)
    if state.platform == "Moxfield":
        state.textresponse = moxinst
    if state.platform == "Archidekt":
        state.textresponse = archinst
    if state.platform == "Plaintext":
        state.textresponse = plaininst
##############################



A = """


<|layout|columns=10px 1fr 5px|
<| |>
<| 

#### Deck upload
Before you upload your deck, there is some important information which you must consider.<br/><br/>

There are a number of different places where you can build a deck. The main ones are Moxfield and Archidekt. Alternatively, if you instead didnt use either of these but would rather enter it manually, please press "plaintext". <br/><br/>

**In general, it is highly recommended that you use one of the two deckbuilding sites. It is much harder to build a deck in plaintext**{: .color-warning} <br/> <br/>
Please select below which platform you used in your analysis. <br/><br/>

<|{platform}|toggle|lov=Moxfield;Archidekt;Plaintext|on_change=textchanger|>
<br/> <br/>
<|{textresponse}|>
|>
<| |>
|>

<br/> <br/>

<|layout|columns=10px 1fr  5px|
<| |>

<|
Once you have completed the above instructions, please upload your file below.
|>

<| |>
|>


__________________________________________
<br/> <br/>
<|layout|columns=10px 1fr 5px|
<| |>
<|
Deck upload: <br/>
<|{cardcsv}|file_selector|label=Select File|on_action=runfunc|extensions=.csv,.xlsx|drop_message=Drop Message|>
|>
<| |>
|>

"""


##############################
###### Page 1 Variables #####
show_pane = False
cardcsv = None
carddf = pd.DataFrame()
carddf["Card Name"] =  "None"
carddf["Converted Mana Cost"] = "None"
carddf["Mana Cost"] =  "None"
carddf["Type"] = "None"
carddf["Oracle Text"] =  "None"
carddf["Power (if creature)"] =  "None"
carddf["Toughness (if creature)"] = "None"


def runfunc(state):
    print(state.cardcsv)
    if ".csv" in state.cardcsv:
        df = pd.read_csv(state.cardcsv, header = None, names = ["cards"])
    if ".xlsx" in state.cardcsv:
        df = pd.read_excel(state.cardcsv, header = None, names = ["cards"])

    notify(state,"info", "Loading Card information, please wait a few seconds.")
    newdf = pd.DataFrame()
    cardcount, name, expac, number, foil = [],[],[],[],[]
    #1 Slimefoot, the Stowaway (CMM) 686 *F*

    #Loading the cards as god intended
    for i in df["cards"]:
        row = i.split(" ")
        cardcount.append(row[0])
        val = 0
        for i in row:
            if "(" in i:
                break
            val += 1

        cardname = ""
        # print(row, val)
        for i in range(val):
            if i + 1 < val:
                cardname = cardname + " " + row[i+1]
            if i+1 == val:
                break
        name.append(cardname)
        

        xpc = row[val]
        xpcs = xpc.split(")")
        xpcs = xpcs[0].split("(")
       

        expac.append(xpcs[1])


        number.append(row[val + 1])

        # print(row, val, len(row))
        if val + 3 == len(row):
            foil.append(1)
        else:
            foil.append(0)

    newdf["Count"] = cardcount
    newdf["Name"] = name
    newdf["Expansion"] = expac
    newdf["setnumber"] = number
    newdf["foil"] = foil

    state.cardcountlist = cardcount
    state.namelist = name
    state.expaclist = expac
    state.setlist = number
    state.foillist = foil 

    print(newdf.head())

    #pulling the data from scryfall with the set number and xpac code and card name

    def scryfall_advanced(set_code, collector_number, card_name):
        url = f"https://api.scryfall.com/cards/{set_code.lower()}/{collector_number}"
        response = requests.get(url)
        if response.status_code == 200:
            response_data = response.json()
            # assert(response_data["name"] == card_name, "Names dont match")
            return response_data
        

    for i in range(len(newdf[newdf.columns[0]])):
        set_code = newdf["Expansion"].iloc[i]
        collect_num = newdf["setnumber"].iloc[i]
        cname = newdf["Name"].iloc[i]
        card_data = scryfall_advanced(set_code, collect_num, cname)
        print(card_data["name"])
        print(card_data["cmc"])
        print(card_data["type_line"])
        print(card_data["oracle_text"])
        print(card_data["image_uris"]["large"])
    
        if i == 1:
            break





    return

exampletable = {
    "Quantity": [1, 1, 12],
    "Card": ["Esior, Wardwing Familiar", "Ishai, Ojutai Dragonspeaker", "Plains"]
}
columns = ["Quantity", "Card"]

##############################


page1_md = """
### **Deck Analysis** {: .color-primary}

In order to use this tool, you should first click the deck upload button below. This will allow you to upload your deck and ensure that the tool is reading your deck correctly. <br/> <br/>
Once you are happy with how it is interpreting your deck, please click the "Run deck analysis" button. This will search through scryfall for the entirety of the information within your deck to ensure that the correct cards are entered. <br/> <br/>

If it looks right in the table below, you can then click the "Run analysis" button below to generate a set of recommendations for your deck, as well as to see some relevant graphics detailing deck statistics. <br/> <br/>

Additionally, if you would like some further calculators to help you with your deck building, a list of relevant deck building / deck testing calculators are available in the "calculators" tab above. <br/> <br/>


<|Deck Upload|button|on_action={lambda state: state.assign("show_pane", True)}|>
<|{show_pane}|pane|partial={partiala}|width=40%|>
<br/> <br/>

____________________________________________________


<br/> <br/>


<|{carddf}|table|rebuild|editable=True|page_size=10|filter[Card Name]=True|filter[Converted Mana Cost]=True|filter[Mana Cost]=True|filter[Type]=True|filter[Power (if creature)]=True|filter[Toughness (if creature)]=True|>



"""


##############################
###### Page 2 Variables #####
def testfunc(state):
    notify(state, "info", "button was pressed", duration = dur)


c1results = None
c2results = None
c3results = None
c4results = None
##############################

page2_md = """
### **Calculators** {: .color-primary}

Below are a list of calculators. These are independent of your uploaded deck in the previous tab, although future updates might remedy this problem.


___________________________________________________________________

##### Calculator 1: Consistent Land Drops



<|Run calculation|button|on_action=testfunc|>

___________________________________________________________________
##### Calculator 2: Turn to have an effect in given normal draws


<|Run calculation|button|on_action=testfunc|>
___________________________________________________________________
##### Calculator 3: Number of mulligans to have an effect in hand

<|Run calculation|button|on_action=testfunc|>

___________________________________________________________________
##### Calculator 4: Number of cards needed to draw to have a full combo


<|Run calculation|button|on_action=testfunc|>

___________________________________________________________________
"""









def on_menu(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)

pages = {
    "/": root_md,
    "Deck": page1_md,
    "Calculators": page2_md
    # "Text": page3_md
}

stylekit = {
    "color_primary": "#C0FFEE",
    "color_secondary": "#BADA55",
    #https://docs.taipy.io/en/release-3.0/manuals/gui/styling/stylekit/
}

gui = Gui(pages=pages)

partiala = gui.add_partial(A)

gui.run(stylekit = stylekit)