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



    
    


