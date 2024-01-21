from taipy.gui import Gui, State
from taipy.gui import Html
from backend import (
    get_api_response,
    get_names_of_meal,
    get_total_info
)
from frontend import stats
from frontend.html_pages import html_page_stats, html_string_stats_0

meal_enter_btn = "ENTER YOUR MEAL"

page = """
#Hey, Welcome to Dhruv, Liz, Naman and Pooja's Web App
<br/>
<|{query}|input|>

<|{meal_enter_btn}|button|on_action=meal_button_press|>

Here are the items you ordered:
<br/>
<br/>
<|{items}|>
<br/>
<br/>

### Here is the nutrition data for your meal today:
<br/>
<|{nutrition}|>

<br/>
### Here is the total nutrition data for your entire day:
<br/>
<|{nutrition_daily}|>

"""


def get_items(api_rep):
    
    print(f"\n I'm the current query")
    
    list_of_items = get_names_of_meal(api_rep)
    return_text = ""
    for index, value in enumerate(list_of_items):
        return_text += value
        if index < len(list_of_items)-1:
            return_text += ", " 
        
    print(f"\n I'm the current return text {return_text}")
    return return_text

total_dict_daily = {
        "Calories": 0.0,
        "Fat": 0.0,
        "Protein": 0.0,
        "Sugar": 0.0,
        "Fiber": 0.0,
        "Carbs": 0.0
    }

def get_nutrition(api_rep):
    
    print(f"\n I'm the current query AGAIN")
    
    dict_of_n = get_total_info(api_rep)
    
    return_text = ""
    for key, value in dict_of_n.items():
        if key == "Calories":
            return_text += f"{key}: {value} cal "
        else:
            return_text += f"{key}: {value} grams "
            
    return return_text

def total_nutrition_calc(api_rep):
    
    global total_dict_daily
    
    
    dict_to_add = get_total_info(api_rep)

    for key, value in dict_to_add.items():
        if key in total_dict_daily:
            total_dict_daily[key] += value
            
    total_dict_daily = {k: round(v, 1) for k, v in total_dict_daily.items()}
            
    return_text = ""
    for key, value in total_dict_daily.items():
        if key == "Calories":
            return_text += f"{key}: {value} cal "
        else:
            return_text += f"{key}: {value} grams "
            
    return return_text
        
def different_inputs():
    
    global total_dict_daily
    
    return total_dict_daily["Calories"], total_dict_daily["Carbs"], total_dict_daily["Sugar"], total_dict_daily["Fat"], total_dict_daily["Fiber"]   

def stats_items_changes():
    

def meal_button_press(state):
    
    print(f"\n I'm at meal button press. ")
    
    api_rep = get_api_response(state.query)
    
    state.items = get_items(api_rep)
    state.nutrition = get_nutrition(api_rep)
    state.nutrition_daily = total_nutrition_calc(api_rep)
    
    stats_items_changes(state)
    

    
    
   
query = ""
items = get_items(get_api_response(query))
nutrition = get_nutrition(get_api_response(query))
nutrition_daily = total_nutrition_calc(get_api_response(query))     


pages= {
    'home_page': page,
    'stats_page': html_string_stats_0
}


Gui(pages = pages).run(dark_mode=True, port = 5001)
