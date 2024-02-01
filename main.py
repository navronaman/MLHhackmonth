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
from frontend import html_pages
from datetime import datetime
from datetime import date
from pytz import timezone
import time
import importlib

# This is content of the buttons
meal_enter_btn = "ENTER YOUR MEAL"
username_enter_btn = "ENTER YOUR USERNAME"

# Home Page
page=("""
#Hey, Welcome to Dhruv, Liz, Naman and Pooja's Web App
<br/>

<|{query_0}|input|>

<|{username_enter_btn}|button|on_action=username_button_press|>
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


# Same page in HTML
page_but_html = Html('''
<h1>Hey, Welcome to Dhruv, Liz, Naman and Pooja's Web App</h1>

<taipy:input>{query_0}</taipy:input>

<taipy:button on_action="username_button_press">{username_enter_btn}</taipy:button>

<taipy:input>{query}</taipy:input>
<taipy:button on_action="meal_button_press">{meal_enter_btn}</taipy:button>

<p>Here are the items you ordered:
<taipy:text>{items}</taipy:text>
</p>

<p>Here is the nutrition data for your meal today:
<taipy:text>{nutrition_daily}</taipy:text>
</p>
                    
<p>Here is the nutrition data for your entire day:
<taipy:text>{nutrition}</taipy:text>
</p>
                    
                     
''')

# Stats Page
html_string_stats_0 = Html(html_pages.return_html_stats())

dhruv_home_page = Html('''
    <head>
        <link href="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js">
        <head><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
        <title>Example</title></head>
    </head>

        <style>
            
            #nav{
                display: flex;
                justify-content: center;
            }
            
            #HomeItem{
                margin-left:15%;
                padding:0.5%;
                height:200%;
                color:white;
            }
            #OtherItem{
                margin-left:20%;
                color:white;
                
            }
            #Goals{
                margin:7%;
                display: flex;
                align-items: center;
                justify-content: center;
                height:150%;
            }
            #meal{
                margin:7%;
                display: flex;
                align-items: center;
                justify-content: center;
                height:150%;
            }
            #submit{
                justify-content: center;
                width:87%;
            }
            .input{
                border-width: 10%;
                border-style: solid;
                border-color: black;
            }
            .card-body{
                display: flex;
                align-items: center;
                justify-content: center;
            }

            #Eat{
                font-size: 200%;
                margin-bottom: 68%;
            }

            #HomeItem:hover, #OtherItem:hover{
                scale:110%;
                transition:0.3s;
                text-decoration: underline;
            }

            #cards{
                display:flex;
                justify-content: space-between;
            }

            .card{
                margin-left:-100%;
            }

            #GoalCard{
                font-size: 200%;
                margin-bottom: 20%;
            }

        </style>

    </head>
    <body style="background-color: rgb(250, 232, 156);">
        
        <!--NavBar-->

        <div id="nav" class="container">
            <nav class="navbar fixed-top navbar-expand-lg navbar-light bg-success">
                <a id="HomeItem" class="navbar-brand" href="#">Home</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav">
                    <a id="OtherItem" class="navbar-brand" href="#">Stats <span class="sr-only">(current)</span></a>
                    <a id="OtherItem" class="navbar-brand" href="#">Reccomendations</a>
                </div>
                </div>
            </nav>
        </div>

          <!--Add Cards for Meal and setting goals-->

        <div id="cards"> 
          <div id="meal" class="card" style="width: 18rem; height:25rem;">  
                <div class="card-body text-center" id="card-body">

                    <div class="container">
                        <h1 class="align-top" id="Eat">
                            What did you eat today?
                            <br>
                        </h1>
                        <small style="font-size:150%" class="text-muted">Add Meals</small>
                        <input class="input" id="input" type="text">
                        <button class="btn btn-info rounded" id="submit">submit</button>
                        <div id="result"></div>
                    </div>
                </div>
            </div>

            <div id="Goals" class="card" style="width: 25rem; height:30rem;">  
                <div class="card-body text-center" id="card-body">

                    <div class="container">
                        <h1 class="align-top" id="GoalCard">
                            What are your goals for today
                            <br>
                        </h1>
                        
                        <div class="input-group mb-3">
                            <div class="input-group-prepend">
                              <span class="input-group-text">cal</span>
                              <span class="input-group-text">Calories</span>
                            </div>
                            <input type="text" class="form-control" aria-label="Amount (to the nearest dollar)">
                          </div>

                          <div class="input-group mb-3">
                            <div class="input-group-prepend">
                              <span class="input-group-text">g</span>
                              <span class="input-group-text">Fiber</span>
                            </div>
                            <input type="text" class="form-control" aria-label="Amount (to the nearest dollar)">
                          </div>

                          <div class="input-group mb-3">
                            <div class="input-group-prepend">
                              <span class="input-group-text">g</span>
                              <span class="input-group-text">Fat</span>
                            </div>
                            <input type="text" class="form-control" aria-label="Amount (to the nearest dollar)">
                          </div>

                          <div class="input-group mb-3">
                            <div class="input-group-prepend">
                              <span class="input-group-text">g</span>
                              <span class="input-group-text">Protein</span>
                            </div>
                            <input type="text" class="form-control" aria-label="Amount (to the nearest dollar)">
                          </div>

                          <button class="btn btn-info rounded" id="submit">Set</button>
                          

                    </div>
                </div>
            </div>
        </div>''')


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
        
def username_button_press(state):
    
    global query_0
    
    print(f"\n I'm at username button press. ")
    
    query_0 = state.query_0
    print(f"\n I'm the current query {query_0}")
    
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
    
    if cloud_dict_of_meal["Nutrition Info"]["Calories"] != 0.0:
        inti_cloud(cloud_dict_of_meal, query_0)
        
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
query_0 = ""
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
    'home_page': page_but_html,
    'stats_page': html_string_stats_0,
    'another_page': dhruv_home_page
}


# Runs Taipy
Gui(pages = pages, css_file='stats.css').run(dark_mode=True, port = 5001)

