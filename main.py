from taipy.gui import Gui, State
from taipy.gui import Html
from backend import (
    get_api_response,
    get_names_of_meal,
    get_total_info
)
from frontend import stats

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

Here is the nutrition data for your meal today:
<|{nutrition}|>

Here is the total nutrition data for your entire day:
<|{nutrition_daily}|>

"""

pages= {
    'home_page': page,
    'stats_page': Html(stats.html_string)
}
stats_page = Html(stats.html_string)

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

def total_nutrition_calc(api_rep):
    
    global total_dict_daily
    
    
    dict_to_add = get_total_info(api_rep)

    for key, value in dict_to_add.items():
        if key in total_dict_daily:
            total_dict_daily[key] += value
            
    return_text = ""
    for key, value in total_dict_daily.items():
        if key == "Calories":
            return_text += f"{key}: {value} cal \n"
        else:
            return_text += f"{key}: {value} grams \n"
            
    return return_text
        

def get_nutrition(api_rep):
    
    print(f"\n I'm the current query AGAIN")
    
    dict_of_n = get_total_info(api_rep)
    
    return_text = ""
    for key, value in dict_of_n.items():
        if key == "Calories":
            return_text += f"{key}: {value} cal \n"
        else:
            return_text += f"{key}: {value} grams \n"
            
    return return_text

def meal_button_press(state):
    
    print(f"\n I'm at meal button press. ")
    
    api_rep = get_api_response(state.query)
    
    state.items = get_items(api_rep)
    state.nutrition = get_nutrition(api_rep)
    state.nutrition_daily = total_nutrition_calc(api_rep)    
    
   
query = "French Fries"
items = get_items(get_api_response(query))
nutrition = get_nutrition(get_api_response(query))
nutrition_daily = total_nutrition_calc(get_api_response(query))     


Gui(pages = pages).run(dark_mode=True, port = 5001)
