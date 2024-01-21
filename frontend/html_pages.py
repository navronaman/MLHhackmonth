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



    
    


