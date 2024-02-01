from taipy.gui import Gui, State

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

def return_html_stats():
    html_string_stats_0 = '''
    <div>
    <section>
        <h2>Daily Calorie Intake</h2>
            <div>
                <div>  
                <taipy:indicator class_name = "calorie_bar" min = "0" max = "{total_calories}" value = "{calorie_counter}" width ="90vw"> Calories: {calorie_counter}</taipy:indicator>
                </div>
            </div>
            <div class = "row">
                <div class="column">
                    <div class="title">
                        <span> Calorie Limit </span>
                    </div>
                    <div class="col_inner">
                        <span> <taipy:text> {total_calories} </taipy:text> </span>
                    </div>
                </div>
                <div class="column">
                    <div class="title">
                        <span> Calorie Remaining </span>
                    </div>
                    <div class="col_inner">
                        <span> <taipy:text> {calorie_counter} </taipy:text> </span>
                    </div>
                </div>
            </div>
            <style>
                .column {
                    float: left;
                    width: 50%;
                    padding: 10px;
                    justify-content:center;
                    }
                .row:after {
                    display: table;
                    clear: both;
                }
                row {
                    height: 20%;
                    width: 100%;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    font-family: 'Roboto', sans-serif;
                    background: #efefef;
                    overflow: hidden;
                    margin-left: 50%;
                }
                .title{
                    font-weight: 300;
                    font-size: 14px;
                    opacity: 0.6;
                    color: #fff;
                    margin-bottom: 6px;
                }
                .col_inner {
                    font-size: 32px;
                    font-weight: 300;
                    color: #fff;
                }
            </style>
            <div class="container">
                <div class="quadrant">
                    <div class="fat">
                        <h2> Fats </h2>
                        <taipy:indicator class_name = "calorie_bar" min = "0" max = "{total_fat}" value = "{fat_counter}" width ="30vw"> Fats: {fat_counter}</taipy:indicator>
                    </div>
                </div>
                <div class="quadrant">
                    <div class="sugar">
                        <h2> Sugar </h2>
                        <taipy:indicator class_name = "sugar_bar" min = "0" max = "{total_sugar}" value = "{sugar_counter}" width ="30vw"> Sugars: {sugar_counter}</taipy:indicator>
                    </div>
                </div>
                <div class="quadrant">
                    <div class="carbs">
                    <h2> Carbs </h2>
                        <taipy:indicator class_name = "carbs_bar" min = "0" max = "{total_carbs}" value = "{carbs_counter}" width ="30vw"> Carbs: {carbs_counter}</taipy:indicator>
                    </div>
                </div>
                <div class="quadrant">
                    <div class="fiber">
                    <h2> Fiber </h2>
                        <taipy:indicator class_name = "fiber_bar" min = "0" max = "{total_fiber}" value = "{fiber_counter}" width ="30vw"> Fibers: {fiber_counter}</taipy:indicator>
                    </div>
                </div>
            </div>
            <style>
                .container{ 
                    width:100%;
                    height:80%;
                    display:grid;
                    grid-template-columns: 50% 50%;
                    grid-row: auto auto;
                    grid-column-gap: 20px;
                    grid-row-gap: 20px;
                    .quadrant{
                        background-color: rgb(0,0,256);
                        padding:20px;
                        display:flex;
                        align-items:center;
                        justify-content:center;
                        border-radius: 20px;
                    }

                }
            </style>
    </section>
    </div>'''
    return html_string_stats_0

def return_html_home():
    html_string_stats_0 = '''
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
        </div>'''
    return html_string_stats_0