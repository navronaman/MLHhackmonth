from taipy.gui import Gui, State
from taipy.gui import Html
from backend import (
    get_api_response,
    get_names_of_meal,
    get_total_info
)
from frontend import stats
from datetime import datetime
from datetime import date
from pytz import timezone
import time
import importlib


''' All the modifiable variables for stats'''
total_calories=100
calorie_counter=0
total_carbs=100
carbs_counter=0
total_sugar=100
sugar_counter=0 
total_fat=100
fat_counter=0 
total_fiber=100
fiber_counter=0
page = """
#Hey, Welcome to Dhruv, Liz, Naman and Pooja's Web App
<br/>
<|{query}|input|>
<br/>
Here are the items you ordered:
<br/>
<br/>
<|{items}|>
<br/>
<br/>

Here is the nutrition data for your meal today:
<|{nutrition}|>

"""

importlib.reload(stats);

pages= {
    'home_page': page,
    'stats_page': Html(stats.CalorieStats(total_calories, calorie_counter, total_carbs, carbs_counter, total_sugar, sugar_counter, total_fat, fat_counter, total_fiber, fiber_counter))
}

def get_items(query):
    
    print(f"\n I'm the current query {query} ")
    
    list_of_items = get_names_of_meal(get_api_response(query))
    return_text = ""
    for index, value in enumerate(list_of_items):
        return_text += value
        if index < len(list_of_items)-1:
            return_text += ", " 
        
    print(f"\n I'm the current return text {return_text}")
    return return_text

def get_nutrition(query):
    
    print(f"\n I'm the current query AGAIN {query}")
    
    dict_of_n = get_total_info(get_api_response(query))
    
    return_text = ""
    for key, value in dict_of_n.items():
        if key == "calories":
            return_text += f"{key}: {value} cal \n"
        else:
            return_text += f"{key}: {value} grams \n"
            
    return return_text

def on_change(state, var_name, var_value):
    if var_name == 'query':
        print("I'm at on_change ")
        state.items = get_items(var_value)
        state.nutrition = get_nutrition(var_value)
    

query = "French Fries"
items = get_items(query)
nutrition = get_nutrition(query)     


current_time = datetime.now(timezone('US/Eastern'))
format = "%H:%M:%S"
ct_string = current_time.strftime(format)
ct_hour = current_time.strftime("%H")

Gui(page = pages['stats_page']).run(dark_mode=True, port = 5001)
time.sleep(20)
