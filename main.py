# For the GUI for the webpage
from taipy.gui import Gui, State, Html, Markdown

# For the internal functions

# Processes the user input into the food api
from backend import (
    get_api_response,
    get_names_of_meal,
    get_total_info,
    get_cloud_dict
)
# Saves user data into the cloud
from cloud import inti_cloud

# For other components
from datetime import datetime, date
from pytz import timezone
import time
import importlib

# This is content of the button
meal_enter_btn = "ENTER YOUR MEAL"

# Home Page
page=("""
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

""")

# Stats Page
html_string_stats_0 = Html('''
<div>
<section>
    <h2>Daily Calorie Intake</h2>
        <div>
            <div> <taipy:text> {calorie_percentage} </taipy:text> </div>
        </div>
    <h2>Calorie Intake</h2>
        <div>
            <div> <taipy:text> {total_calories} </taipy:text> </div>
        </div>
    <h2>Calories Remaining</h2>
        <div>
            <div> <taipy:text> {calories_remaining} </taipy:text> </div>
        </div>
</section>
</div>
''')


# Gets items from the api
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

# Gets nutrition 
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

# Global dictionary
total_dict_daily = {
        "Calories": 0.0,
        "Fat": 0.0,
        "Protein": 0.0,
        "Sugar": 0.0,
        "Fiber": 0.0,
        "Carbs": 0.0
    }


# Updates global dictionary
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
        
# Function #1 when the state changes (user presses the button)    
def meal_button_press(state):
    
    global total_dict_daily
    
    print(f"\n I'm at meal button press. ")
    
    api_rep = get_api_response(state.query)
    
    # Displaying items on the home page
    state.items = get_items(api_rep)
    state.nutrition = get_nutrition(api_rep)
    state.nutrition_daily = total_nutrition_calc(api_rep)
    
    # Cloud
    cloud_dict_of_meal = get_cloud_dict(api_rep)
    
    current_time = datetime.now()
    
    inti_cloud(cloud_dict_of_meal, current_time)
        
    # Updating stats page
    stats_items_changes(state, total_dict_daily) 
   
# Function #2 when the state changes 
def stats_items_changes(state, total_dict_daily):
    
    state.calorie_counter = total_dict_daily["Calories"]
    state.carbs_counter = total_dict_daily["Carbs"]
    state.sugar_counter = total_dict_daily["Sugar"]
    state.fat_counter = total_dict_daily["Fat"]
    state.fiber_counter = total_dict_daily["Fiber"]
    
    state.total_calories = 2000
    state.total_carbs = 100
    state.total_sugar = 100
    state.total_fat = 100
    state.total_fiber = 70
    
    state.calorie_percentage = round(state.calorie_counter / state.total_calories * 100)
    state.sugar_percentage = round(state.sugar_counter / state.total_sugar * 100)
    state.carbs_percentage = round(state.carbs_counter / state.total_carbs * 100)
    state.fat_percentage = round(state.fat_counter / state.total_fat * 100)
    state.fiber_percentage = round(state.fiber_counter / state.total_fiber * 100)

    state.calories_remaining = state.total_calories - state.calorie_counter
    state.sugar_remaining = state.total_sugar - state.sugar_counter
    state.carbs_remaining = state.total_carbs - state.carbs_counter
    state.fat_remaining = state.total_fat - state.fat_counter
    state.fiber_remaining = state.total_fiber - state.fiber_counter
   
    
   
# Default values for all the assignments
query = ""
items = get_items(get_api_response(query))
nutrition = get_nutrition(get_api_response(query))
nutrition_daily = total_nutrition_calc(get_api_response(query))     

calorie_counter = 0
carbs_counter = 0
sugar_counter = 0
fat_counter = 0
fiber_counter = 0

total_calories = 2000
total_carbs = 100
total_sugar = 100
total_fat = 100
total_fiber = 70

calorie_percentage = 0
sugar_percentage = 0
carbs_percentage = 0
fat_percentage = 0
fiber_percentage = 0

calories_remaining = 0
sugar_remaining = 0
carbs_remaining = 0
fat_remaining = 0
fiber_remaining = 0


# Stores the HTML pages in a string for Taipy
pages= {
    'home_page': page,
    'stats_page': html_string_stats_0
}


# Runs Taipy
Gui(pages = pages, css_file='stats.css').run(dark_mode=True, port = 5001)

