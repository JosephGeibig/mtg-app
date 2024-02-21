from taipy.gui import Gui, notify

text = "test"
file = None
pip1 = 0
pip2 = 1


page = """
<|toggle|theme|>


<|layout|columns=1 1|
<|
My text: <|{text}|>

Enter a word:
<|{text}|input|>
|>

<|
Plesae upload your decklist
<|{file}|file_selector|>
|>
|>
"""



Gui(page).run() #use_reloader=True



# Upload a file: 
# <|{content}|file_selector|>

# |>

# <|Table|expandable|
# <|{dataframe}|table|width=100%|>
# |>
# |>