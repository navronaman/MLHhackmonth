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

    
html_string_stats_0 = '''
<section class = "MainCalorie" id="Calories">
            <h2>Daily Calorie Intake</h2>
            <div class = "container">
                <div class = "calorie"> <taipy:text> {calorie_percentage} </taipy:text> %</div>
            </div>
            <h3> Calorie Limit: {total_calories} </h3>
            <h4> Calories Remaining: {calories_remaining} </h4>
        </section>
        <style>
            .MainCalorie h2{
                text-align: center;
            }
            .MainCalorie h3{
                text-align: center;
            }
            .MainCalorie h4{
                text-align: center;
                color: rgb(256,0,0);
            }
            .container{
                background-color: rgb(192, 192, 192); 
                width: 80%; 
                border-radius: 15px; 
            }
            .calorie{
                color: white; 
                padding: 1%; 
                text-align: right; 
                font-size: 20px; 
                border-radius: 15px; 
                background-color: rgb(0, 0, 256); 
                width: {calorie_percentage}%;
            }
        </style>
<title> Other Metrics </title>
        <style>
            #gridSection {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                grid-template-rows: repeat(2, 1fr);
                gap: 10px;
                height: 500px; 
            }
            .quadrant {
                padding: 20px;  
                text-align: center;
            }
            .circProgressSugar::before {
                color: rgb(0,0,256);
                content: "{sugar_percentage}% \A Total Sugars: {total_sugar}g \A Sugar Remaining: {sugar_remaining}g";
                display: flex;
                justify-content: center;
                align-items: center;
                position: absolute;
                width:200px;
                height: 200px;
                white-space: pre;
                font-size: 14px;
            }
            .circProgressSugar {
                position: relative;
                display: flex;
                justify-content: center;
                align-items: center;
                margin-left: 50%;
                margin-top: 10%;
                width: 200px;
                height: 200px;
                border-radius: 50%;
                background: 
                radial-gradient(closest-side, rgb(255, 255, 255) 79%, transparent 80% 100%),
                conic-gradient(blue {sugar_percentage}%, grey 0);    
            }
            .circProgressCarbs::before {
                color: rgb(0,0,256);
                content: "{carbs_percentage}% \A Total Carbs: {total_carbs}g \A Sugar Remaining: {carbs_remaining}g";
                display: flex;
                justify-content: center;
                align-items: center;
                position: absolute;
                width:200px;
                height: 200px;
                white-space: pre;
                font-size: 14px;
            }
            .circProgressCarbs {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-left: 50%;
                margin-top: 50px;
                width: 200px;
                height: 200px;
                border-radius: 50%;
                background: 
                radial-gradient(closest-side, rgb(255, 255, 255) 79%, transparent 80% 100%),
                conic-gradient(blue {carbs_percentage}%, grey 0);    
            }
            .circProgressFiber::before {
                color: rgb(0,0,256);
                content: "{fiber_percentage}% \A Total Fibers: {total_fiber}g \A Fiber Remaining: {fiber_remaining}g";
                display: flex;
                justify-content: center;
                align-items: center;
                position: absolute;
                width:200px;
                height: 200px;
                white-space: pre;
                font-size: 14px;
            }
            .circProgressFiber {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-left: 50%;
                margin-top: 50px;
                width: 200px;
                height: 200px;
                border-radius: 50%;
                background: 
                radial-gradient(closest-side, rgb(255, 255, 255) 79%, transparent 80% 100%),
                conic-gradient(blue {fiber_percentage}%, grey 0);    
            }
            .circProgressFat::before {
                color: rgb(0,0,256);
                content: "{fat_percentage}% \A Total Fat: {total_fat}g \A Sugar Remaining: {fat_remaining}g";
                display: flex;
                justify-content: center;
                align-items: center;
                position: absolute;
                width:200px;
                height: 200px;
                white-space: pre;
                font-size: 14px;
            }
            .circProgressFat {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-left: 50%;
                margin-top: 50px;
                width: 200px;
                height: 200px;
                border-radius: 50%;
                background: 
                radial-gradient(closest-side, rgb(255, 255, 255) 79%, transparent 80% 100%),
                conic-gradient(blue {fat_percentage}%, grey 0);    
            }
            .quadrant h2{
                margin-left: 20%;
            }
        </style>
        <section id="gridSection">
            <div class="quadrant">
            <h2> Sugar </h2>
                <div class = "circProgressSugar">
                    <progress value = "30" min ="0" max = "100" style="visibility:hidden;height:0;width:0;"></progress>
                </div>
            </div>
            <div class="quadrant">
            <h2> Carbs </h2>
            <div class = "circProgressCarbs">
                    <progress value = "70" min ="0" max = "100" style="visibility:hidden;height:0;width:0;"></progress>
                    
                </div>
            </div>
            <div class="quadrant">
            <h2> Fat </h2>
            <div class = "circProgressFat">
                    <progress value = "70" min ="0" max = "100" style="visibility:hidden;height:0;width:0;">30%</progress>
                </div>
                </div>
            <div class="quadrant">
            <h2> Fiber </h2>
            <div class = "circProgressFiber">
                    <progress value = "70" min ="0" max = "100" style="visibility:hidden;height:0;width:0;">30%</progress>
                </div>
                </div>
        </section>'''

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